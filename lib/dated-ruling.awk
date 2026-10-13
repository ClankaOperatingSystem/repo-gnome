# CANON-2: a sentence that names a decision and a date together.
BEGIN {
  decide = "(ruled|ruling|decided|decision|agreed|accepted|approved|settled|chose)"
  month = "(January|February|March|April|May|June|July|August|September|October|November|December)"
  date = "([0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]|[0-9][0-9]? " month " [0-9][0-9][0-9][0-9]|" month " [0-9][0-9][0-9][0-9])"
  pattern = decide ".{0,40}" date "|" date ".{0,40}" decide
}
function judge(file, line, text) {
  if (tolower(text) ~ pattern || text ~ pattern)
    report(file, line, "CANON-2 dated ruling", text)
}
