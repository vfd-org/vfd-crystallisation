"""Markov adapter. Shell = total-variation distance to stationary (mixing shell);
boundary = stationary distribution. Ergodic chain CLOSES (gap<1)."""
import numpy as np

def run():
    P = np.array([[0.1,0.8,0.05,0.05],[0.05,0.1,0.8,0.05],[0.05,0.05,0.1,0.8],[0.8,0.05,0.05,0.1]])
    ev = np.sort(np.abs(np.linalg.eigvals(P)))[::-1]
    gap = float(1 - ev[1])
    pi = np.real(np.linalg.eig(P.T)[1][:, np.argmin(np.abs(np.linalg.eig(P.T)[0]-1))]); pi/=pi.sum()
    return dict(second_eig=float(ev[1]), spectral_gap=gap,
                outcome="CLOSED" if gap > 1e-9 else "CRITICAL",
                certificate="spectral gap 1-|lambda_2|>0 + stationary measure pi (contraction on mean-zero)",
                stationary=[float(x) for x in pi])

if __name__ == "__main__":
    import json; print(json.dumps(run(), indent=2, default=str))
