# Walk the prose lines of Org and Markdown files, leaving out what a canon
# check does not judge: code and example blocks, quote blocks, property
# drawers, comments, and in Org the body of a task, a heading with a TODO
# keyword, down to the next heading. For each prose line it calls
# judge(FILENAME, FNR, line), which the check's own awk file defines, and
# at the end exits 1 if the check set any finding, else 0.
#
# Text between double quotation marks, straight or curly, is blanked
# before judge sees the line, and the marks are kept, so that a check
# sees that a quotation is there and not the words inside it. A
# quotation may run over several lines of a paragraph, and a blank line
# ends it.
#
#   awk -f lib/prose.awk -f lib/check.awk FILE...
FNR == 1 { skip = 0; drawer = 0; task = 0; in_straight = 0; in_curly = 0 }
/^[ \t]*$/ { in_straight = 0; in_curly = 0; next }
/^[ \t]*#\+(begin|BEGIN)_(src|SRC|example|EXAMPLE|quote|QUOTE)/ { skip = 1; next }
/^[ \t]*#\+(end|END)_(src|SRC|example|EXAMPLE|quote|QUOTE)/ { skip = 0; next }
/^[ \t]*```/ { skip = !skip; next }
/^[ \t]*:PROPERTIES:/ { drawer = 1; next }
/^[ \t]*:END:/ { drawer = 0; next }
skip || drawer { next }
/^\*+ / {
  task = ($0 ~ /^\*+ (TODO|NEXT|WAITING|SOMEDAY|DONE|CANCELLED|STARTED|HOLD) /)
  if (!task) judge(FILENAME, FNR, plain($0))
  next
}
task { next }
/^[ \t]*#/ && !/^[ \t]*#\+/ { next }
{ judge(FILENAME, FNR, plain($0)) }

# The text of a line with the inside of each quotation removed.
# in_straight and in_curly say whether a straight or a curly quotation
# is open at the end of the line.
function plain(text,   out, rest, i, c) {
  out = ""
  rest = text
  while (length(rest) > 0) {
    if (in_straight) {
      i = index(rest, "\"")
      if (!i) return out
      in_straight = 0; out = out "\""; rest = substr(rest, i + 1)
    } else if (in_curly) {
      i = index(rest, "”")
      if (!i) return out
      in_curly = 0; out = out "”"; rest = substr(rest, i + length("”"))
    } else {
      i = index(rest, "\""); c = index(rest, "“")
      if (!i && !c) return out rest
      if (i && (!c || i < c)) { out = out substr(rest, 1, i); in_straight = 1; rest = substr(rest, i + 1) }
      else { out = out substr(rest, 1, c - 1) "“"; in_curly = 1; rest = substr(rest, c + length("“")) }
    }
  }
  return out
}

function report(file, line, message, text) {
  sub(/^\.\//, "", file)
  sub(/^[ \t]+/, "", text)
  if (length(text) > 80) text = substr(text, 1, 80)
  print file ":" line ": " message ": " text
  any = 1
}
END { exit any ? 1 : 0 }
