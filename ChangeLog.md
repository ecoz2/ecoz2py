2020-05

- build adjustments as c code now uses openmp.
  Build successful on:
    - macos with  gcc (Homebrew GCC 9.3.0_1) 9.3.0


2020-04

- expose ecoz2_vq_learn and test with preliminary callback for wandb 
  use callback(m, avg_distortion, sigma, inertia)
- expose ecoz2_set_random_seed
- upgrade ecoz2 pointer (now 0.2.0)

- initial run with wandb
  https://app.wandb.ai/carueda/whale/runs/24s9w4xz

- preliminaries for an ecoz2py module based on cffi
- expose hmm_learn
    
- in general module to be imported as `import ecoz2py as ecoz2`
  and functions called as eg. `ecoz2.prd_show_file(...)`

2020-03

- initial skeleton, first with cython, then cffi
