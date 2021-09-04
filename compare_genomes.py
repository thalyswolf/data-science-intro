cont = {}

for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont[i+j] = 0


def generate_genom_html(input, output):
    input_data = open(input).read()
    input_data = input_data.replace('\n', '')

    output_data = open(output, 'w')

    for k in range(len(input_data) - 1):
        cont[input_data[k] + input_data[k+1]] += 1

    i = 1

    for k in cont:
        alpha = cont[k] / max(cont.values())

        html = "<div style='width: 100px; border: 1px solid #111; height: 100px; float: left; background-color:rgba(0, 0, 0, " + \
        str(alpha) + "); color: #fff;'>" + k + "</div>"
        output_data.write(html)

        if i%4 == 0:
            output_data.write("<div style='clear:both'></div>")

        i += 1

    output_data.close()

generate_genom_html('./data/human.fasta', './outputs/human_genom.html')
generate_genom_html('./data/bacteria.fasta', './outputs/bacteria_genom.html')
