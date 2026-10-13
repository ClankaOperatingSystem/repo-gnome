# Walk the prose lines of Org and Markdown files, leaving out what a canon
# check does not judge: code and example blocks, quote blocks, property
# drawers, comments, and in Org the body of a task, a heading with a TODO
# keyword, down to the next heading. For each prose line it calls
# judge(FILENAME, FNR, line), which the check's own awk file defines, and
# at the end exits 1 if the check set any finding, else 0.
#
#   awk -f lib/prose.awk -f bin/check.awk FILE...
FNR == 1 { skip = 0; drawer = 0; task = 0 }
/^[ \t]*#\+(begin|BEGIN)_(src|SRC|example|EXAMPLE|quote|QUOTE)/ { skip = 1; next }
/^[ \t]*#\+(end|END)_(src|SRC|example|EXAMPLE|quote|QUOTE)/ { skip = 0; next }
/^[ \t]*```/ { skip = !skip; next }
/^[ \t]*:PROPERTIES:/ { drawer = 1; next }
/^[ \t]*:END:/ { drawer = 0; next }
skip || drawer { next }
/^\*+ / {
  task = ($0 ~ /^\*+ (TODO|NEXT|WAITING|SOMEDAY|DONE|CANCELLED|STARTED|HOLD) /)
  if (!task) judge(FILENAME, FNR, $0)
  next
}
task { next }
/^[ \t]*#/ && !/^[ \t]*#\+/ { next }
{ judge(FILENAME, FNR, $0) }
function report(file, line, message, text) {
  sub(/^\.\//, "", file)
  sub(/^[ \t]+/, "", text)
  if (length(text) > 80) text = substr(text, 1, 80)
  print file ":" line ": " message ": " text
  any = 1
}
END { exit any ? 1 : 0 }
