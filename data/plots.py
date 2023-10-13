import numpy as np # linear algebra
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay,auc
# from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, classification_report, accuracy_score, roc_curve, 
auc

# create receiver operating characteristic(ROC) curve
# i.e. how well is our model performing?
def createROC(fpr,tpr):
    fig = plt.figure()
    ax = fig.add_subplot()

    plt.plot([0, 1], [0, 1], 'k-.', label = 'Random prediction')
    plt.plot(fpr, tpr, label = 'Logistic regression model: AUC = %0.4f' % auc(fpr, tpr))
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve for Logistic Regression')

    ax.grid(False)
    plt.legend()
    # plt.show()
    # plt.save?
    plt.savefig('coderep_ROC.png')

# -----------------------    

# Confusion matrix plot
def displayConfusionMatrix(cm, model):
    disp = ConfusionMatrixDisplay(confusion_matrix = cm,
                                  display_labels = model.classes_)
    
    disp.plot()
    plt.grid(visible = False)
    plt.title('Confusion matrix')
    # plt.show()
    plt.savefig('coderep_ConfMat.png')

# -----------------------    

# Logistic plot
def logistic_regression_plot(features,data_df, Diagnosis):
    fig = plt.figure(figsize = (11, 5))
    for i, feature in enumerate(features):
        ax = fig.add_subplot(1, 3, i + 1)
        sns.regplot(data = data_df,
                    x = feature, 
                    y = Diagnosis, 
                    logistic = True, 
                    color = 'black',
                    line_kws = {'lw' : 1, 'color' : 'red'},
                    label = str(feature.replace('_', ' ').capitalize()))
        ax.set_xlabel(str(feature.replace('_', ' ').capitalize()))
        plt.ylabel('Probability')
        plt.title('Logistic regression')
        plt.legend()
    
        plt.tight_layout()
        # plt.show()
        plt.savefig('coderep_Log_plot.png')

    return None

# ---------------

# Box & whisker plot routine
def makeBoxplot(features,data_df, Diagnosis, xtickmarks):
    fig = plt.figure(figsize = (8, 12))
    for i, feature in enumerate(features):
        ax = fig.add_subplot(2, 2, i + 1)
        sns.boxplot(x = Diagnosis, 
                   y = feature, 
                   data = data_df, 
                   showfliers = True)
        plt.title(str(feature.replace('_', ' ').capitalize()))
        ax.set_xticklabels(xtickmarks)
        ax.set_xlabel(Diagnosis.capitalize())
        ax.set_ylabel(str(feature.replace('_', ' ').capitalize()))
        ax.grid(False)
    
    fig.tight_layout()
    # plt.show()
    plt.savefig('coderep_boxplot.png')

# ---------------

def createHeatmap(input_data):
    sns.set_theme(style ='white')
    #Generate a mask for the upper triangular matrix
    mask = np.triu(input_data.corr(), k = 0)

    fig = plt.figure(figsize = (18, 18))
    ax = fig.add_subplot()

    # Generate a custom diverging palette of colours
    cmap = sns.diverging_palette(230, 20, as_cmap = True)

    sns.heatmap(data = input_data.corr(), 
                annot = True, 
                linewidths = 0.5, 
                fmt = '.1f',
                ax = ax, 
                mask = mask,
                cmap = cmap)

    plt.title('A correlation heatmap of the features', fontsize = 20)
    # plt.show()
    plt.savefig('coderep_heatmap.png')

# ---------------

#Plot histogram
def makeHistogram(features,Malignant,Benign,bins):
    for feature in features:
        if not type(feature) is str:
            raise TypeError('Only strings are permitted')
            
    fig = plt.figure(figsize = (10, 8))
    for i, feature in enumerate(features):
        ax = fig.add_subplot(1, 3, i + 1)  
        sns.histplot(Malignant[feature], 
                   bins = bins, 
                   color = 'red', 
                   label = 'Malignant',
                   kde = True)
        sns.histplot(Benign[feature], 
                   bins = bins, 
                   color = 'green', 
                   label = 'Benign',
                   kde = True)
        plt.title(str(' Distribution of  ') + str(feature.replace('_', ' ').capitalize()))
        plt.xlabel(str(feature.replace('_', ' ').capitalize()))
        plt.ylabel('Density function')
        plt.legend(loc = 'upper right')
        ax.grid(False)
    
    plt.tight_layout()
    # plt.show()
    plt.savefig('coderep_histogram.png')

# ---------------

def createCountplot(data_df, xtickmarks):
    fig = plt.figure(figsize = (8, 6))
    ax = fig.add_subplot()

    sns.set_theme(style = 'whitegrid')

    sns.countplot(data = data_df, 
              x = data_df.diagnosis, 
              label = 'Count',
              lw = 4,
              ec = 'black').set(title = 'A count of benign and malignant tumours',
                                  xlabel = 'Diagnosis',
                                  ylabel = 'Count')

    ax.set_xticklabels(xtickmarks)
    # plt.show()
    plt.savefig('coderep_countplot.png')

# ---------------
    
