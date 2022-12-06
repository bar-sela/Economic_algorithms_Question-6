import math

import matplotlib.pyplot as plt
import networkx as nx

"""
 במטלה זו - התבקשנו שבהינתן גרף עם יחסי ערכים חיובים, 
 - צריך להחזיר פלט של מעגל שמכפלת אורכיי משקליו אכן קטנה מ1 ->שקול למעגל שסכום מlog של משקליו קטן מ 0 . 
  אחרת - להחזיר כי אין מעגל שכזה בגרף . בתכנית זו השתמשתי באלגוריתם בלמן פורד שנמצא בספריה nx .
  

"""

#### יצירת גרף עם צלעות

def serch_negative_cycle(G):
    #החלק של התחום הוא קוד מהאינטרנט שיוצר גרף ויזואלי על מנת לעזור לבודק בהבנה .
    ##################### ####################################3 ###########
    elarge = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] > 0.5]
    esmall = [(u, v) for (u, v, d) in G.edges(data=True) if d["weight"] <= 0.5]

    pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

    # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # edges
    nx.draw_networkx_edges(G, pos, edgelist=elarge, width=6)
    nx.draw_networkx_edges(
        G, pos, edgelist=esmall, width=6, alpha=0.5, edge_color="b", style="dashed"
    )

    # node labels

    ax = plt.gca()
    ax.margins(0.08)
    plt.axis("off")
    plt.tight_layout()

    ##################### ####################################3

    """
    לכל צלע בגרף אנחנו רוצים להפוך את משקלה לlog(w)
    כך שנוכל להתעסק עם למצוא מעגל שלילי בגרף במקום למצוא מעגל שהכפל של המשקלים בו הוא קטן 1 , נובע מחוקי לוגים
    """
    for u,v,d in G.edges(data=True):   ## הפיכת כל צלע לlog של הצלע
           d['weight'] = math.log2(d['weight'])


    print(G.edges(data=True)) ## הדפסת כל המידע על הגרף כך שהמשתמש יוכל לראות את הפלט גם בטרמינל ולא רק ויזואלית
    """
    אנחנו מפעילים את הפונקציה find_negative_cycle שבספריה nx. הפונקציה הזו מתבססת על אלגוריתם בלמן פורד כך שאם לא  מזוהה מעגל שלילי אז 
    נזרקת שגיאה . במקרה זה נתפוס את השגיאה ונדפיס למשתמש כי אין מעגל שלילי בגרף , במקרה השני נדפיס את המעגל השלילי - בצורה כזו ['a', 'b', 'a']} לדוגמא  
    """
    try:
        a = (nx.find_negative_cycle(G, "a", weight="weight"))
        b = (nx.find_negative_cycle(G, "b", weight="weight"))
        c = (nx.find_negative_cycle(G, "c", weight="weight"))
        d = (nx.find_negative_cycle(G, "d", weight="weight"))
        print("the negative cycle is :")
        print(a)
    except:
        print("there is no negative cycle ")

        ## שורות קוד מהאינטנט לתצוגה ויזואלית

    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    plt.show()





