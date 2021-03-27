 #!/usr/bin/env bash

#for samples in 1000 2000 5000 10000 20000 50000 100000 200000 500000
for samples in 1000 2000 5000 10000 20000 50000 100000
do
    python prep_nopg_dataset.py --env_name maze2d-umaze-v1 --n_samples ${samples}
    python prep_nopg_dataset.py --env_name pendulum-v0 --n_samples ${samples}
    python prep_nopg_dataset.py --env_name cartpolestabilization-v1 --n_samples ${samples}
done

