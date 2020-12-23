import os

if __name__ == "__main__":
    # os.system("python main.py --env_name traffic_junction --nagents 20 --nprocesses 1 --num_epochs 2000 --eval_epoch 50 --hid_size 128 --detach_gap 10 --lrate 0.001 --dim 18 --commnet --vision 3 --recurrent --add_rate_min 0.02 --add_rate_max 0.05 --curr_start 250 --curr_end 1250 --difficulty hard --max_steps 40 --mean_ratio 0 --transformer --comm_round 2 --save models/transformer.pkl")
    os.system("python main.py --env_name traffic_junction --nagents 20 --nprocesses 1 --num_epochs 2000 --eval_epoch 50 --hid_size 128 --detach_gap 10 --lrate 0.001 --dim 18 --ic3net --vision 3 --recurrent --add_rate_min 0.02 --add_rate_max 0.05 --curr_start 250 --curr_end 1250 --difficulty hard --max_steps 40")

