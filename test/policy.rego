package AccessControl

default allow = false

allow {
    input.request.query.user == "alice"
}
