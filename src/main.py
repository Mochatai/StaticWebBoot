from textnode import TextNode
from htmlnode import HTMLNode
from blocksFunc import markdown_to_html_node
import re
import os
import shutil
import sys
def clean_public():
    path_to_clean = "docs"
    content_to_delete = os.listdir(path_to_clean)

    for content in content_to_delete:
        p = os.path.join(path_to_clean,content)
        if os.path.exists(p) == False:
            raise Exception("path is not working clean_copy_public")
        if os.path.isfile(p):
            os.remove(p)
            continue
        
        elif os.path.isdir(p):
            shutil.rmtree(p)

def get_all_content_paths(p):
     path_to_copy = p
     files_paths = {}

     path_contents = os.listdir(p)

     for content in path_contents:
         content_path = os.path.join(path_to_copy,content)

         if os.path.isfile(content_path):
             files_paths[content_path] = "file"
             continue
         
         elif os.path.isdir(content_path):
             files_paths[content_path] = "dir"
             temp = get_all_content_paths(content_path)
             files_paths.update(temp)

     return files_paths

def get_dis_files(paths_content, src_path):
    str_dis = src_path
    dic_dis = {}

    for content in paths_content.keys():
        loc = content.find("/")
        str_edit = content[loc:]

        dic_dis[f'{str_dis}{str_edit}'] = paths_content[content]
    
    return dic_dis

def copy_content(table_contents, dis_src1):
    dis_p = get_dis_files(table_contents, dis_src1)
    
    count = 0
    for content in table_contents.keys():

        if table_contents[content] == "dir":
            os.mkdir(list(dis_p)[count])
            count += 1
            continue

        elif table_contents[content] == "file":
            shutil.copy(content,list(dis_p)[count])
            count += 1
            continue

    
def one_to_one_copy(source_file, dis_file, ty):


    if ty == "dir":
            os.mkdir(dis_file)
            
            

    elif ty == "file":
            shutil.copy(source_file, dis_file)
            






     

def clean_copy_public():
    clean_public()
    tes = get_all_content_paths("static")
    copy_content(tes, "docs")
      



def extract_title(markdown: str):
    markdown_first_line = markdown.splitlines()
    h_count = re.search(r"^#+ ", markdown_first_line[0])
    if h_count.end() - 1 > 1:
        raise Exception("no h1 tags")
    
    markdown_strip = str(markdown_first_line[0])
    markdown_strip_clean = markdown_strip[h_count.end():]

    return markdown_strip_clean

def generate_page(from_path, template_path, dest_path, base_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')

    with open(from_path, 'r', encoding='utf-8') as from_path_file:
        from_path__content = from_path_file.read()
    
    with open(template_path, 'r', encoding='utf-8') as template_file:
        template_path_content = template_file.read()

    html_string = markdown_to_html_node(from_path__content)
    html_string = html_string.to_html()
    page_title = extract_title(from_path__content)
    template_with_title = template_path_content.replace("{{ Title }}", str(page_title))
    template_with_title_content = template_with_title.replace("{{ Content }}", html_string)
    template_with_title_content_href = template_with_title_content.replace(f'href="/"', f'href="{base_path}"')
    template_with_title_content_href_src = template_with_title_content_href.replace(f'src="/"', f'src="{base_path}"')


    dest_path_clean = dest_path[:-2]
    dest_path_clean_html = dest_path_clean + "html"

    with open(dest_path_clean_html, "w", encoding="utf-8") as file:
        file.write(template_with_title_content_href_src)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, base_path):
    souce_content = get_all_content_paths(dir_path_content)
    dis_content = get_dis_files(souce_content,  dest_dir_path)
    #print("get_all_content", souce_content)
    #print("get_dis_files", dis_content)

    count = 0
    for content in souce_content.keys():

        if souce_content[content] == "dir":
            os.mkdir(list(dis_content)[count])
            count += 1
            continue

        elif souce_content[content] == "file":

            if f'{content[-2]}{content[-1]}' == "md":
                generate_page(content, template_path, list(dis_content)[count], base_path)
                count += 1
                continue

            shutil.copy(content,list(dis_content)[count])
            count += 1
            continue

def main():

    cli_input_len = len(sys.argv)

    if (cli_input_len - 1) < 1:
        basepath = "/"

    else:
        basepath = sys.argv[1]

    

    clean_copy_public()
    generate_pages_recursive("content", "template.html", "docs", basepath)



if __name__ == "__main__":
    main()