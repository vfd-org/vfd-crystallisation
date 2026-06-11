\\ Generate zeta zeros to height 2500 for the GUE ledger row (row 10).
\\ Run: gp -q out/_zeta_zeros.gp   -> writes out/zeta_zeros.txt
default(parisizemax, 2000000000);
default(realprecision, 28);
z = lfunzeros(1, 2500);
f = "out/zeta_zeros.txt";
system("rm -f out/zeta_zeros.txt");
for (i = 1, #z, write(f, z[i]));
print(#z, " zeros written");
quit
