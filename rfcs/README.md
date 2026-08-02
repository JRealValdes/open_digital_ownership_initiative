# Requests for Comments (RFCs)

Large or contentious changes to the Digital Ownership Framework should
be proposed as RFCs before they are merged into `docs/framework.md`.

## When to write an RFC

Write an RFC if your change:

- Adds a new ownership mode, right, or actor.
- Changes how ownership is represented, transferred, or recovered.
- Introduces a protocol, cryptographic design, or marketplace rule with
  ecosystem-wide impact.
- Substantially expands or narrows the scope of the initiative.

Small clarifications, wording fixes, and glossary updates usually do
**not** need an RFC—open a normal pull request instead.

## Process

1. Copy [`0000-template.md`](0000-template.md) to a new file:
   `NNNN-short-title.md` (use the next available number).
2. Fill in the template and open a pull request.
3. Discuss and revise in the pull request.
4. If accepted, update the framework (and glossary/FAQ as needed), then
   mark the RFC as **Accepted**.

## Status meanings

| Status     | Meaning                                      |
|------------|----------------------------------------------|
| Draft      | Under discussion                             |
| Accepted   | Approved; framework updates may follow       |
| Rejected   | Not adopted                                  |
| Superseded | Replaced by a later RFC                      |
| Withdrawn  | Author withdrew the proposal                 |
