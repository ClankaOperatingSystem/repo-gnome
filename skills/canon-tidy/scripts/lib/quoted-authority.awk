# CANON-8: a line of prose that frames a quotation as its author's authority.
BEGIN {
  name = "([Tt]he [a-z]+|[A-Z][A-Za-z.]*( [A-Z][A-Za-z.]*)?)"
  frame = "[Ii]n " name "'s (words|formulation|terms)|" name "'s (own )?words|[Aa]s " name " (said|put it|wrote)|" name " (said|wrote):"
  quoted = name " (ruled|decided|deferred|asked|said)[^\"“]*[\"“]"
}
function judge(file, line, text) {
  if (text ~ frame || text ~ quoted)
    report(file, line, "CANON-8 quoted authority", text)
}
