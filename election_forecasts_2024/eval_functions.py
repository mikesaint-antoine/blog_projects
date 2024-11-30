
import numpy as np





def brier_score(y_pred, y_true):

    assert len(y_pred) == len(y_true)

    total = 0

    for i in range(len(y_pred)):

        total += (y_pred[i] - y_true[i])**2

    total = total / len(y_pred)

    return(total)





def calibration(y_true,y_score,bin_bounds=[0,0.2,0.4,0.6,0.8,1]):
    assert len(y_true) == len(y_score)

    error = 0

    bin_means = []
    outcome_means = []
    outcome_stds = []
    pred_means = []
    bin_counts = []


    for i in range(len(bin_bounds)-1):

        total = 0
        happened = 0

        outcomes = []
        preds = []

        for j in range(len(y_score)):

            score = y_score[j]

            if score >= bin_bounds[i] and score < bin_bounds[i+1]:


                total += 1

                happened += y_true[j]
                outcomes.append(y_true[j])
                preds.append(score)


        if total > 0:
            bin_means.append(np.mean([bin_bounds[i],bin_bounds[i+1]]))
            outcome_means.append(np.mean(outcomes))
            outcome_stds.append(np.std(outcomes))
            pred_means.append(np.mean(preds))
            bin_counts.append(total)



    return([bin_means, outcome_means, pred_means, bin_counts])






def make_calibration_plot(outcomes, probs, title="", plot_file="", scaling_factor=4):


    [bin_means, outcome_means, pred_means, bin_counts] = calibration(outcomes,probs)


    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec


    # credit to ChatGPT for this plotting code


    # Create a figure with two subplots, one for the scatter plot and one for the table
    fig = plt.figure(figsize=(12, 6))  # Adjust figure size as needed
    gs = gridspec.GridSpec(1, 2, width_ratios=[2, 1])  # 2:1 ratio to give more space to the plot

    # Scatter plot on the left
    ax_plot = plt.subplot(gs[0])
    ax_plot.set_ylim(-0.05, 1.05)  # Add padding above 1
    ax_plot.set_xlim(-0.05, 1.05)  # Add padding on the x-axis as well

    sizes = [count * scaling_factor for count in bin_counts]

    ax_plot.scatter(bin_means, outcome_means, s=sizes)
    ax_plot.set(autoscale_on=False, aspect='equal')
    perfect, = ax_plot.plot([0, 1], [0, 1], color="black", label="perfect")
    ax_plot.legend(handles=[perfect], fontsize=12, loc=4)
    ax_plot.set_title(title, fontsize=16)
    ax_plot.set_xlabel("Prediction Probability", fontsize=12)
    ax_plot.set_ylabel("Outcome Fraction", fontsize=12)

    # Table on the right
    ax_table = plt.subplot(gs[1])

    # Hide axes for the table subplot
    ax_table.xaxis.set_visible(False)
    ax_table.yaxis.set_visible(False)
    ax_table.set_frame_on(False)

    # Prepare the table data
    table_rows = []
    for i in range(len(bin_means)):
        tmp = [round(bin_means[i], 3), bin_counts[i], round(pred_means[i], 3), round(outcome_means[i], 3)]
        table_rows.append(tmp)

    columns = ["Bin Center", "Count", "Pred. Mean", "Outcome"]

    # Create the table
    table = ax_table.table(cellText=table_rows, colLabels=columns, cellLoc='center', loc='center')

    # Style the table
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1.5, 1.5)  # Adjust scaling for better fit

    # Alternate row colors and highlight header row
    header_color = '#40466e'  # Dark header background color
    header_text_color = 'white'
    row_colors = ['#f1f1f2', 'white']  # Alternating row colors

    for (i, j), cell in table.get_celld().items():
        if i == 0:
            # Header row
            cell.set_text_props(color=header_text_color)  # White text
            cell.set_facecolor(header_color)  # Dark background
            cell.set_fontsize(12)
        else:
            # Alternate row colors for data rows
            cell.set_facecolor(row_colors[i % len(row_colors)])

    # Adjust the layout to make sure the table isn't cut off
    plt.tight_layout(pad=2.0)  # Increase padding between subplots

    # Save the figure with bbox_inches to avoid cutting off the table
    plt.savefig(plot_file, dpi=1000, bbox_inches='tight')