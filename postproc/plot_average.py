import matplotlib

matplotlib.use('Agg')
from matplotlib import gridspec
import matplotlib.pyplot as plt
import pandas as pd
from ipdb import set_trace as bp
import sys, os
from basic_functions import createExpFolderandCodeList

EXPERIMENT_ID = sys.argv[1]
METRICS = ['f1','acc','ap','auc','precis','recall']
#series_exp = [range(411,420), range(421,430),range(431,440),range(441,450),range(451,460),range(461,470),range(471,480),range(481,490),range(491,500),range(501,510),
series_exp = [range(701,710),range(711,420), range(721,730),range(731,740),range(741,750),range(751,760),range(761,770),range(771,780),range(781,790),range(791,800)]

# paths
path_experiments = '../../experiments'
path_save = os.path.join(path_experiments, EXPERIMENT_ID)

# create exp folder
createExpFolderandCodeList(path_save)

# iterate over metrics
for metric in METRICS:
    average_df = pd.DataFrame()
    for series in series_exp:
        average_dict = {}
        for risk_level, exp_id in enumerate(series):
            df = pd.read_csv(os.path.join(path_experiments, str(exp_id), 'metrics.csv'))
            average_dict[str(risk_level)] = df[metric][0]
        # update Dataframe
        average_df = average_df.append(average_dict, ignore_index=True)

    # compute average and std of averages
    mean = average_df.mean()
    std = average_df.std()

    # plot figure
    plt.figure()
    plt.plot(range(1,len(mean)+1),mean)
    plt.fill_between(range(1,len(mean)+1), mean-std, mean+std, color = 'blue', alpha = 0.15)
    plt.xlabel('Risk Level')
    plt.ylabel(metric.capitalize())
    plt.savefig(os.path.join(path_save, metric+'.pdf'))
    plt.close()

    # save res in csv
    average_df.loc['mean'] = mean
    average_df.loc['std'] = std
    average_df.to_csv(os.path.join(path_save,metric+'.csv'))
