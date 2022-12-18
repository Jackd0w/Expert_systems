sattelite(nomer1).
sattelite(nomer2).
00
get_conn(S, relay) :- sattelite(S).
get_infra(S, signal) :- get_conn(S, relay).
get_photo(S, signal) :- get_conn(S, relay).
establish_conn(S, signal) :- get_conn(S, relay), get_infra(S, signal), get_photo(S, signal).