# CANON-7: a line of prose that says where work stands.
BEGIN {
  words = "not yet|planned:|none yet|is not built|has been used once|remains to be|awaits? |untested|never run|for now|interim|work in progress"
  heads = "^(\\*+|#+) +(open questions|gaps|known limitations|status)[ \t]*$"
}
function judge(file, line, text,   low) {
  low = tolower(text)
  if (low ~ words || low ~ heads)
    report(file, line, "CANON-7 status in canon", text)
}
