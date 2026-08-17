# LEARNX — AI Learning Failure Diagnosis & Recovery Engine

LEARNX is an advanced e-learning platform that uses Bayesian Knowledge Tracing and diagnostic engines to identify exactly where and why a student is struggling with programming concepts, offering targeted interventions.

## Production Security Requirement (IMPORTANT)

**Phase 4 currently ships with a Development-Only Fallback Runner.**

The code execution sandbox uses Python and Node.js subprocesses running natively on the host machine. While this fallback utilizes temporal isolated directories, strict timeouts, and payload size limitations, **it does NOT provide comprehensive OS-level filesystem or network isolation.**

### DO NOT deploy this runner to a public-facing production environment.

In order to securely deploy LEARNX in production and support untrusted user code execution, an actual isolation boundary must be integrated, such as:
1. Docker Container Sandbox (e.g., executing code inside ephemeral, network-disabled, unprivileged containers).
2. VM / microVMs (e.g., Firecracker).
3. Third-party isolated execution API (e.g., Judge0, Piston).

Deploying the current development runner to production exposes the host operating system to severe security vulnerabilities, including arbitrary file reading/writing and local network scanning.
