from wordcloud import WordCloud

wc = WordCloud()
wc.generate_from_text('This is a word cloud example which has a few words, showing them word for word in a cloud.')

svg_text = wc.to_svg()
with open('test.svg', 'w') as f:
    f.write(svg_text)