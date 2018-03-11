import plotly
import plotly.graph_objs as go
import numpy as np
import plotly.plotly as py


def create_chart(overall_result,tag_results =''):

    """

    :param overall_result: This is the overall results stats
    :param tag_results:  These are tags in the output.xml
    :return: html widget
    """
    html_data = ''

    ## Overall percentage graph
    overall_list = []



    ## Total Execution Report
    if overall_result != '':
        overall_list.append(int(overall_result['pass']))
        overall_list.append(int(overall_result['fail']))
        fig = {
          "data": [
            {
              "values": overall_list,
              "labels": [ "Pass", "Fail" ],
                'marker': {'colors': ['rgb(12, 227, 107)',
                                      'rgb(255, 94, 51)']},
              "domain": {"x": [0, .48]},
              "name": "Total Test Case ",
              "hoverinfo":"label",
              "hole": .4,
              "type": "pie"
            }
        ],
          "layout": {
                "title":"Total Execution Percentage",
                "annotations": [
                    {
                        "font": {
                            "size": 10
                        },
                        "showarrow": False,
                        "text": "Total Percenatage",
                        "x": 0.20,
                        "y": 0.5
                    }
                ] ,

            }

        }
        # plotly.offline.plot(fig, filename='donut.html',validate=False)
        total_percentage = plotly.offline.plot(fig, output_type = 'div' )
        html_data += total_percentage




    ## Print the statistics based in tags
    passed_values = []
    failed_values = []
    tag_list = []

    for key,value in tag_results.items():
        tag_list.append(key)

    for tags in tag_list:
        passed_values.append(tag_results[tags]['pass'])
        failed_values.append(tag_results[tags]['fail'])

    trace1 = go.Bar(
        x=tag_list,
        y=passed_values,
        name='Passed'
    )
    trace2 = go.Bar(
        x=tag_list,
        y=failed_values,
        name='Failed'
    )

    data = [trace1, trace2]
    layout = go.Layout(
        title="Tag wise percentage",

        barmode='group'
    )

    group_bar = go.Figure(data=data, layout=layout)
    # plotly.offline.plot(fig, filename='grouped-bar.html',validate=False)

    cust_wise_percent = plotly.offline.plot(group_bar, output_type='div')
    html_data += cust_wise_percent
    return html_data
