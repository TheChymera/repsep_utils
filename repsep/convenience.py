import pandas as pd
import os

latex_class = r'\documentclass[border=2pt]{standalone}'
latex_preamble = r"""\providecommand{\e}[1]{\ensuremath{\times 10^{#1}}}
\usepackage{amsmath}
\usepackage{booktabs}
"""
latex_template = r"""%s
%s
\begin{document}
\pagenumbering{gobble}
%s
\end{document}
"""


def repsep_create_table_tex(infile, outfile):
    df = pd.read_csv(infile, index_col=0)
    df = df.fillna('N/A')
    tex_table = df.style.to_latex()
    tex_document = latex_template % (latex_class, latex_preamble, tex_table)
    with open(outfile, 'w') as output:
        output.write(tex_document)
