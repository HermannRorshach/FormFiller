from docx import Document
from docx.shared import Pt

# Открываем документ
doc = Document('template.docx')

def search_redact_paragraph(index):
    paragraph = doc.paragraphs[index]
    for run in paragraph.runs:
        run_text = run.text.strip()
        if run_text.startswith('<') and run_text.endswith('>'):
            return True
    return False

def redact_paragraph(index, line):
    # Получаем первый параграф
    paragraph = doc.paragraphs[index]
    p_style = paragraph.style
    line_spacing = paragraph.paragraph_format.line_spacing
    p_alignment = paragraph.alignment

    # Создаем новый параграф
    new_paragraph = doc.add_paragraph(style=p_style)
    new_paragraph.paragraph_format.line_spacing = line_spacing
    new_paragraph.alignment = p_alignment
    if new_paragraph.alignment:
        print('True')


    # Проходимся по всем Run в текущем параграфе
    for run in paragraph.runs:
        run_text = run.text.strip()
        if not run_text.startswith('<') and not run_text.endswith('>'):
            # Копируем Run в новый параграф
            new_run = new_paragraph.add_run(run.text)
            # Копируем форматирование
            new_run.bold = run.bold
            new_run.italic = run.italic
            new_run.underline = run.underline
            new_run.font.size = run.font.size
        else:
            #print('Мы нашли искомый ран!')
            print(run.text)
            new_run = new_paragraph.add_run()
            # Копируем форматирование
            new_run.bold = run.bold
            new_run.italic = run.italic
            new_run.underline = run.underline
            new_run.font.size = run.font.size
            new_run = new_paragraph.add_run(line)
            new_run.bold = True
            new_run.font.size = Pt(15)

    # Вставляем новый параграф перед текущим
    index = list(doc.element.body).index(paragraph._element)
    doc.element.body.insert(index, new_paragraph._element)

    # Удаляем исходный параграф
    doc.element.body.remove(paragraph._element)

indexes = []
lines = ["АЗЕРБАЙДЖАНСКАЯ РЕСПУБЛИКА ИРАН", "Иванова", "Глиссандра", "Рюриковна"]
for index in range(len(doc.paragraphs)):
    if search_redact_paragraph(index):
        indexes.append(index)
for index, line in zip(indexes, lines):
    redact_paragraph(index, line)
# Сохраняем изменения
doc.save('test2.docx')
