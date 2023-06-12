import matplotlib.pyplot as plt

run_pre = ""
run_fine = ""

jobs_pre = {

            "": ""}
jobs_fine = {
             "": ""}




#### PRETRAINING ####
job_pre = jobs_pre[run_pre]
if job_pre == "":
    pass
elif job_pre == "":
    1

### FINE TUNING ###
job_fine = jobs_fine[run_fine]
if job_fine == "":
    pass
elif job_fine == "":
    1


#### PLOTTING PRE TRAINING ####
if run_pre != "":
    # Plot data on each subplot
    fig, axs = plt.subplots(2, 3, figsize=(8, 5))
    axs[0, 0].plot(loss)
    axs[0, 1].plot(loss_t)
    axs[1, 0].plot(loss_f)
    axs[1, 1].plot(loss_c)
    axs[1, 2].plot(loss_TF)

    axs[0, 0].set_title('Average loss')
    axs[0, 1].set_title('Average loss time')
    axs[1, 0].set_title('Average loss frequency')
    axs[1, 1].set_title('Average loss c')
    axs[1, 2].set_title('Average loss TF')

    plt.tight_layout()
    plt.suptitle(f"Pre-training, {run_pre}")
    plt.subplots_adjust(top=0.88)
    plt.show()


##### PLOTTING FINE TUNE #####
if run_fine != "":
    fig, axs = plt.subplots(2, 2, figsize=(7, 6))
    axs[0, 0].plot(Finetune_Accuracies)
    axs[0, 1].plot(Finetune_Losses)
    axs[1, 0].plot(Test_Accuracies)
    axs[1, 1].plot(Test_Losses)

    axs[0, 0].set_title('Finetune accuracy')
    axs[0, 1].set_title('Finetune loss')
    axs[1, 0].set_title('Test accuracy')
    axs[1, 1].set_title('Test loss')

    plt.tight_layout()
    plt.suptitle(f"Fine-tuning, {run_fine}")
    plt.subplots_adjust(top=0.88)
    plt.show()