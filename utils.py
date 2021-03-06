import tkinter
from ldr.loader_base import LoaderBase


def fillTextBoxAtStartup(combat_box, runes_box, converge_box, runes_spin, op_spin, ship_stat_spin, guild_box):
    lcs = locals()
    boxes_to_fill = []
    spin_frames_to_fill = []
    for i in lcs:
        if type(lcs[i]) is tkinter.Text or type(lcs[i]) is tkinter.ttk.Entry:
            boxes_to_fill.append(i)
        else:
            spin_frames_to_fill.append(i)

    text = LoaderBase().file_content
    fill_ranges = {
        'combat_box': (0, 9),
        'runes_box': (9, 17),
        'converge_box': (17, 18),
        'spinbox_r1r': 18,
        'spinbox_r1l': 19,
        'spinbox_r2r': 20,
        'spinbox_r2l': 21,
        'spinbox_op': 22,
        'guild_box': (23, 25),
        'spinbox_virt': 25,
        'spinbox_orbs': 26,
        'spinbox_orbl': 27,
        'spinbox_lege': 28,
        'spinbox_ascd': 29,
        'spinbox_asch': 30,
        'spinbox_trph': 31,
        'spinbox_trpd': 32,
    }

    try:
        for box in boxes_to_fill:
            tmp = ''
            for i in range(fill_ranges[box][0], fill_ranges[box][1]):
                tmp += text[i]
            start = '0.0' if type(locals()[box]) is tkinter.Text else '0'
            locals()[box].insert(start, tmp[:-1])

        for spin_frame in spin_frames_to_fill:
            for key in [k for k in locals()[spin_frame].__dict__ if k.find('spinbox') != -1]:
                locals()[spin_frame].__dict__[key].insert('0', text[fill_ranges[key]][:-1])

    except IndexError:
        return False

    return True


def saveFromTextBoxToFile(combat_box, runes_box, converge_box, runes_spin, op_spin, guild_box, ship_stat_spin):
    try:
        with open("iou.txt", 'w') as file:
            tmp = ''
            tmp += combat_box.get('0.0', 'end')
            tmp += runes_box.get('0.0', 'end')
            tmp += converge_box.get() + "\n"
            tmp += runes_spin.spinbox_r1r.get() + "\n"
            tmp += runes_spin.spinbox_r1l.get() + "\n"
            tmp += runes_spin.spinbox_r2r.get() + "\n"
            tmp += runes_spin.spinbox_r2l.get() + "\n"
            tmp += op_spin.spinbox_op.get() + "\n"
            tmp += guild_box.get('0.0', 'end')
            tmp += ship_stat_spin.spinbox_virt.get() + "\n"
            tmp += ship_stat_spin.spinbox_orbs.get() + "\n"
            tmp += ship_stat_spin.spinbox_orbl.get() + "\n"
            tmp += ship_stat_spin.spinbox_lege.get() + "\n"
            tmp += ship_stat_spin.spinbox_ascd.get() + "\n"
            tmp += ship_stat_spin.spinbox_asch.get() + "\n"
            tmp += ship_stat_spin.spinbox_trph.get() + "\n"
            tmp += ship_stat_spin.spinbox_trpd.get() + "\n"
            file.write(tmp)
        return True
    except IndexError:
        return False
