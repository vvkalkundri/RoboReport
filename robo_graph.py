import xml.etree.ElementTree as etree
from StringIO import StringIO

from chart import create_chart


def data_calculator(file_name):

    """

    :param file_name: Output.xml
    :return:
    """
    with open(file_name) as f:
        xml = f.read()
    context = etree.iterparse(StringIO(xml))
    overall_result = dict()
    list_of_tags = []
    tag_results = {}
    execution_time = ''

    for action, elem in context:
        if elem.tag == 'tag':
            list_of_tags.append(elem.text)
        if elem.tag == 'stat':
            try:
                if elem.text == 'All Tests':
                    if elem.attrib.items()[0][0] == "fail":
                        overall_result['fail'] = elem.attrib.items()[0][1]
                    if elem.attrib.items()[1][0] == "pass":
                        overall_result['pass'] = elem.attrib.items()[1][1]
                if elem.text in list_of_tags:
                    tag_results[elem.text] = {}
                    if elem.attrib.items()[0][0] == "fail":
                        tag_results[elem.text]["fail"] = int(elem.attrib.items()[0][1])
                    if elem.attrib.items()[1][0] == "pass":
                        tag_results[elem.text]["pass"] = int(elem.attrib.items()[1][1])
            except:
                continue

    return overall_result,tag_results


def robo_graph_generator():

    overall_result,tag_results = data_calculator('output.xml')
    total_pass = int(overall_result['pass'])
    total_fail = int(overall_result['fail'])
    total_result = total_pass + total_fail



    all_test_case_data ="""<div align="center" style="vertical-align:bottom">
<div align="center" style="vertical-align:bottom">
<table border="1" align="centre">
<tr bgcolor = 0CE36B align="center"><th>Total Test Cases</th><th>Passed</th><th>Failed</th></tr>
<tr><th>"""+str(total_result)+"""</th><th>"""+ str(total_pass) +"""</th><th>"""+ str(total_fail) +"""</th></tr>
</table></div></div>"""


    html_data = create_chart(overall_result,tag_results)
    html= "<html><head><meta charset=\"utf-8\" /></head><H1 align=\"center\"> Automation execution summary"+"</H1><body>"+all_test_case_data+"<script type=\"text/javascript\">/**" + html_data + "</script></body></html>"
    f = open("graph.html",'w+')
    f.write(html)
    f.close()



if __name__ == "__main__":
    robo_graph_generator()