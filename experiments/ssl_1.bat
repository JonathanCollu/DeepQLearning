python experiment.py ^
-use_img ^
-ssl_mode 2 ^
-net ssl_cnn ^
-loss mse ^
-optimizer adam ^
-optim_lr 1e-4 ^
-rb_size 5000 ^
-batch_size 128 ^
-n_episodes 1000 ^
-gamma 0.99 ^
-target_model ^
-tm_wait 5 ^
-policy egreedy ^
-epsilon 0.025 0.99 1000. ^
-run_name C:/Users/ricca/Desktop/exp_results/ssl_1