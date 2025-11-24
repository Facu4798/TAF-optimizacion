import matplotlib.pyplot as plt
import seaborn as sns
import os

def make_graph(tickers, series):
    os.makedirs('webapp/static/graphs/', exist_ok=True)
    for image in os.listdir('webapp/static/graphs/'):
        os.remove(os.path.join('webapp/static/graphs/', image))
    plt.figure(figsize=(15,5)).tight_layout()
    for t in tickers:
        sns.lineplot( x=series[t].index, y=series[t]['Close'][t], label=t)
    plt.legend(loc='upper left', fontsize='x-large')
    plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
    plt.savefig('webapp/static/graphs/report.png', bbox_inches='tight',dpi=600)
    plt.clf()