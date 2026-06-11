default(realprecision, 20);
E = ellinit([0,-1,1,-10,-20]);   \\ 11a1, explicit coeffs, no DB lookup
print("START");
L = lfuncreate(E);
print("LCREATED");
zs = lfunzeros(L, 14);
print("COND=", ellglobalred(E)[1]);
print("ZEROS=", zs);
print("AP=", vector(60, n, if(isprime(n), ellap(E,n), 0)));
print("DONE");
