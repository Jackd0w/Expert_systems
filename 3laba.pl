define(sattelite, connection).

get_conn(sattelite, relay) :- define(sattelite, connection).
get_infra(sattelite, signal) :- get_conn(sattelite, relay).
get_photo(sattelite, signal) :- get_conn(sattelite, relay).
establish_conn(sattelite, signal) :- get_conn(sattelite, relay), get_infra(sattelite, signal), get_photo(sattelite, signal).
