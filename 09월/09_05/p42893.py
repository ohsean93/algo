def solution(word, pages):
    word = word.lower()
    doc = dict()
    i = -1
    for page in pages:
        i += 1
        page = page.lower()
        cut_page = page.split('head')[1]
        link = []
        url_cut_html = ''
        for cut_html in cut_page.split('\"'):
            if 'https://' in cut_html:
                url_cut_html = cut_html.split('https://')[1]
        if 'href=\"https://' in page:
            for link_url_cut in page.split('<a href=\"https://')[1:]:
                link.append(link_url_cut.split('\\n')[0].split('\"')[0])
        if '\n' in url_cut_html:
            url_cut_html = ''

        cut_page = page
        for char in range(128):
            if 97 <= char <= 122 or 65 <= char <= 90:
                continue
            else:
                cut_page = ' '.join(cut_page.split(chr(char)))
        url = url_cut_html

        cnt = 0

        for w in cut_page.split():
            if w == word:
                cnt += 1
        if link:
            link_point = cnt / len(link)
        else:
            link_point = 0
        if url:
            doc[url] = [i, cnt, link_point, link, 0]  # 인덱스, 기본점수, 링크점수(반환값), 링크 리스트, 포인트

    answer = -1
    point = -1
    for info in doc.values():
        info[4] += info[1]
        for link_url in info[3]:
            if doc.get(link_url):
                sub_info = doc[link_url]
                sub_info[4] += info[2]

    for info in doc.values():
        url_point = info[4]

        if url_point > point:
            point = url_point
            answer = info[0]
    print(doc)

    return answer