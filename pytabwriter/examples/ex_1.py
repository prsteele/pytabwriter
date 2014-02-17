text = """Lorem ipsum dolor sit amet,\tconsectetur adipiscing elit.\tInteger
libero turpis, \tlacinia sed hendrerit \teleifend, commodo a
augue. \tVestibulum ante ipsum primis in faucibus \torci luctus et
ultrices \tposuere cubilia Curae; \tProin molestie est congue velit
euismod aliquam. \tCum sociis natoque penatibus \tet magnis dis parturient
montes, \tnascetur ridiculus mus. \tAliquam mattis sit amet urna vel
dapibus. \tUt et risus at est consequat \teleifend ut eget neque. Praesent
aliquet elit \tligula, nec molestie mauris \tornare placerat."""

if __name__ == '__main__':
    from pytabwriter import TabWriter
    tw = TabWriter()
    tw.write(text)

    print('original (with tabs removed)')
    print(text.replace('\t', ''))
    print('')
    print('left-aligned')
    print(str(tw))
    print('')
    print('center-aligned')
    tw.alignment = 'c'
    print(str(tw))
    print('')
    print('right-aligned')
    tw.alignment = 'r'
    print(str(tw))
    
