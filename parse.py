import os
import re
import pypinyin


def getSlug(name):
    py = pypinyin.lazy_pinyin(name)
    slug = []
    for i in range(0, len(py) - 1):
        slug.append(py[i])
    # concatenate slug using '-', but not add in middle
    str = ''

    if slug[0][-1] == ' ':
        str += slug[0][:-1]
    else:
        str += slug[0]

    str += '-'

    for i in range(1, len(slug) - 1):
        # ommit space
        if slug[i] != ' ':
            str += slug[i] + '-'
    str += slug[-1]
    str = str.replace(' ', '-')
    print("INFO: " + str)
    return str


def addFrontMatter(path, slug, title):
    with open(path, 'r+', encoding="utf-8") as f:
        # read first line to check if it is ---
        lines = f.readlines()
        # the file pointer will move to the next line, so move back
        f.seek(0)
        frontMatters = ["---\n"]
        endLineNumber = 0
        if lines[0] == '---\n':  # if it is ---, then it already has front matter
            for line in range(1, len(lines)):
                if lines[line] == '---\n':
                    endLineNumber = line + 1
                    break
                frontMatters.append(lines[line])
            # add front matter
            frontMatters.append('title: ' + title + '\n')
            frontMatters.append('slug: ' + slug + '\n')
            frontMatters.append('---\n')
        else:
            frontMatters.append('title: ' + title + '\n')
            frontMatters.append('slug: ' + slug + '\n')
            frontMatters.append('---\n')

        print("INFO: " + str(frontMatters) + "for file: " + path)

        # write to file
        for line in frontMatters:
            f.write(line)
        # write the rest of the file
        for line in lines[endLineNumber:]:
            f.write(line)


def main():
    cwd = os.getcwd()
    # print(os.listdir(cwd + "/content"))
    content_dir = cwd + '/content'
    content_list = os.listdir(content_dir)

    for file in content_list:
        # if filename contains chinese, then add slug to it
        if re.search(r'[\u4e00-\u9fa5]', file):
            with open(content_dir + '/' + file, 'r') as f:
                addFrontMatter(content_dir + '/' + file,
                               getSlug(file), file[:-3])  # remove '.md'
        else:
            # no chinese in filename, then only replace space to dash
            with open(content_dir + '/' + file, 'r') as f:
                addFrontMatter(content_dir + '/' + file,
                               file[:-3].replace(' ', '-'), file[:-3])


if __name__ == "__main__":
    main()
