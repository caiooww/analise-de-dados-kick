from fpdf import FPDF

class PDF(FPDF):

    def titulo(self, label):
        self.set_font('helvetica', 'B', size=24)
        self.cell(0, 60, label, 0, 1, 'C')

    def sub_titulo(self, label):
        self.set_font('helvetica', 'I', size=16)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def linha_centralizada(self, label):
        self.set_font('helvetica', '', size=12)
        self.cell(0, 10, label, 0, 1, 'C')
    
    def titulo_base(self, label):
        self.set_font('helvetica', 'B', size=16)
        self.cell(0, 8, label, 0, 1, 'L')
        self.ln()
        
    def destaque(self, label):
        self.set_font('helvetica', 'B', size=14)
        self.cell(0, 4, label, 0, 1, 'L')
        self.ln()

    def paragrafo(self, text):
        self.set_font('helvetica', '', size=12)
        self.multi_cell(0, 6, text)
        self.ln()

    def imagem(self, img, x, y, w):
        self.image(img, x, y, w)

pdf = PDF()

# ------------- Fazendo a capa -------------
pdf.add_page()

pdf.titulo("Análise da Desigualdade na Educação Brasileira")
pdf.sub_titulo("Utilizando dados públicos para entender os problemas")
pdf.imagem("capa.webp", 40, 90, 130)
pdf.ln(160)
pdf.linha_centralizada("Autor: Caio Augusto")
pdf.linha_centralizada("Data: 7 de Setembro de 2024")


pdf.add_page()

pdf.titulo_base("Introdução")

pdf.paragrafo("A educação, a chave que abre portas para um futuro melhor, enfrenta desafios sérios no Brasil. Milhões de jovens e adultos buscam conhecimento, mas encontram obstáculos como a falta de escolas de qualidade, especialmente nas regiões mais afastadas e em comunidades com menos recursos. As diferenças sociais e as complexidades da gestão escolar criam um cenário desigual, onde nem todos têm as mesmas oportunidades de aprender e crescer ")

pdf.paragrafo("O Brasil precisa de uma educação superior que prepare todos os seus jovens para o futuro. Mas será que essa oportunidade está disponível para todos? Neste relatório, vamos investigar se a qualidade da educação varia de acordo com a região do país e o tipo de instituição. Nosso objetivo é identificar os desafios e propor soluções para construir um sistema educacional mais justo e eficiente, que beneficie a todos os brasileiros.")

pdf.paragrafo("Para realizar este estudo, utilizamos um banco de dados gigantesco do Ministério da Educação, com informações sobre mais de 900 mil cursos de graduação em todo o Brasil. Nesses dados, encontramos detalhes como o nome da faculdade, se ela é pública ou privada, o tipo de curso (medicina, direito, pedagogia, etc.), se as aulas são presenciais ou online, quantas vagas são oferecidas e onde fica localizada. Com tantas informações, conseguimos ter uma visão bem completa da educação superior no nosso país.")




pdf.add_page()

pdf.titulo_base("Desenvolvimento")

pdf.destaque(" Distribuição de vagas por Região")

pdf.paragrafo("Ao observar os dados de vagas e cursos de graduação, percebemos que o Sudeste e o Nordeste concentram a maior parte das oportunidades de ensino superior no Brasil. Essa diferença se explica, em parte, pelo maior número de habitantes e pela presença de grandes cidades nessas regiões. No entanto, essa concentração cria um cenário desigual, onde as outras regiões do país podem ficar para trás na disputa por vagas e qualidade de ensino.")


pdf.imagem("grafico_cursosregiao.png", 40, 90, 130)

pdf.add_page()


pdf.imagem("graficosVagasregiao.png", 40, 196, 130)


pdf.add_page()

pdf.paragrafo('Quando olhamos para os números de cursos presenciais e online em cada região do Brasil, percebemos que, apesar de muitos cursos serem oferecidos à distância, essa oferta não é a mesma em todos os lugares. Por que será que algumas regiões têm mais opções de cursos online do que outras? Uma das explicações pode estar na falta de internet de qualidade ou de computadores em algumas regiões, o que dificulta o acesso aos cursos online. Além disso, as políticas de cada estado e as necessidades dos estudantes também podem influenciar essa diferença.')

pdf.imagem("Gráfico_Modalidade_por_Região.png", 40, 50, 130)
pdf.ln(130)


pdf.add_page()
pdf.destaque(" Modalidades de Ensino")

pdf.paragrafo("Se formos comparar os números, a diferença entre os cursos presenciais e online é enorme. Quase 9 em cada 10 cursos no Brasil são oferecidos à distância. Essa mudança mostra como a educação a distância se tornou a principal opção para quem quer fazer uma faculdade.")




pdf.paragrafo("Cada vez mais brasileiros estão escolhendo estudar à distância. Por quê? A flexibilidade de horário, a possibilidade de estudar de qualquer lugar e o preço mais acessível são alguns dos motivos que fazem da educação online uma opção tão popular.")

pdf.paragrafo("Mas nem tudo são flores. Para aproveitar bem os cursos online, é preciso ter acesso à internet de qualidade e a equipamentos como computador. Além disso, é importante garantir que a qualidade do ensino seja a mesma dos cursos presenciais, para que os estudantes tenham todo o apoio necessário.")

pdf.paragrafo("É importante lembrar que estudar online não significa deixar de lado as aulas presenciais. Muitas faculdades oferecem cursos que misturam as duas modalidades, permitindo que os alunos tenham o melhor dos dois mundos.")



pdf.add_page()

pdf.imagem("graficoModalidade_Especial.png", 40, 90, 130)
pdf.add_page()
pdf.imagem("graficoModalidade_Privada com fins lucrativos.png", 40, 90, 130)
pdf.add_page()
pdf.imagem("graficoModalidade_Privada sem fins lucrativos.png", 40, 90, 130)
pdf.add_page()
pdf.imagem("graficoModalidade_Pública Estadual.png", 40, 90, 130)
pdf.add_page()
pdf.imagem("graficoModalidade_Pública Federal.png", 40, 90, 130)
pdf.add_page()
pdf.imagem("graficoModalidade_Pública Municipal.png", 40, 90, 130)

pdf.add_page()


pdf.ln(70)

pdf.destaque(" A Situação dos Cursos")

pdf.paragrafo("A boa notícia é que a maioria dos cursos de graduação no Brasil estão funcionando a todo vapor. Isso significa que temos uma oferta bem ampla de opções para quem quer fazer uma faculdade.")

pdf.paragrafo("A taxa de extinção de cursos apresenta uma significativa variabilidade entre as diferentes regiões do país, evidenciando a influência de fatores locais sobre a sustentabilidade dos programas de graduação.")
pdf.imagem("graficoSituacao.png", 35, 140, 130)


pdf.add_page()

pdf.imagem("graficosVagasregiao.png", 35, 10, 130)

pdf.ln(110)

pdf.destaque(" Relação de Categorias Administrativas por Região")

pdf.paragrafo("A oferta de ensino superior no Brasil é marcada pela forte presença de instituições privadas com fins lucrativos, especialmente no Sudeste. Embora a proporção dessas instituições varie entre as regiões, o setor privado se destaca em todas elas.")

pdf.paragrafo(" As instituições especiais, como as comunitárias e filantrópicas, embora desempenhem um papel importante no setor educacional, apresentam uma participação relativamente pequena na oferta de ensino superior em todas as regiões do país..")


pdf.add_page()

pdf.imagem("graficoCategorias_admCENTRO-OESTE.png", 40, 10, 150)
pdf.imagem("graficoCategorias_admNORDESTE.png", 40, 110, 150)
pdf.imagem("graficoCategorias_admNORTE.png", 40, 210, 150)

pdf.add_page()
pdf.imagem("graficoCategorias_admSUL.png", 40, 10, 150)
pdf.imagem("graficoCategorias_admSUDESTE.png", 40, 110, 150)

pdf.ln(190)

pdf.paragrafo("A concentração do setor privado pode levar a uma mercantilização da educação, priorizando o lucro em detrimento da qualidade e da equidade no acesso.")



pdf.add_page()

pdf.titulo_base("Conclusão")

pdf.paragrafo("A análise da oferta de ensino superior no Brasil revela um quadro marcado por contrastes. A expansão da educação a distância e a presença de instituições privadas demonstram a dinâmica do setor. No entanto, a concentração de vagas em determinadas regiões e a desigualdade de acesso, especialmente para estudantes de baixa renda, exigem ações mais efetivas do poder público. A garantia de qualidade na educação a distância, a ampliação da oferta de vagas em regiões menos favorecidas e o apoio a estudantes de baixa renda são desafios urgentes a serem enfrentados para construir um sistema de ensino superior mais justo e inclusivo")


pdf.output("relatório.pdf")