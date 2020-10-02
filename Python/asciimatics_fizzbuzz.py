#!/usr/bin/env python3

# requirement: pip install asciimatics
# https://github.com/peterbrittain/asciimatics

from asciimatics.effects import Scroll, Mirage, Cycle
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from asciimatics.exceptions import ResizeScreenError
import sys

def _fizzbuzz(screen):
    scenes = []

    fb, fc, fp, ff = {}, {}, {}, {}
    for i in range(1,101):
        fp[i] = (i-1) * 8
        if i % 3 == 0 and i % 5 == 0:
            fb[i] = "FizzBuzz"
            fc[i] = 6
            ff[i] = "banner3"
        elif i % 3 == 0:
            fb[i] = "Fizz"
            fc[i] = 3
            ff[i] = "banner3"
        elif i % 5 == 0:
            fb[i] = "Buzz"
            fc[i] = 7
            ff[i] = "banner3"
        else:
            fb[i] = str(i)
            fc[i] = 2
            ff[i] = "banner3"

    effects = [
        Scroll(screen, 3),
        Mirage(
            screen,
            FigletText(fb[1], font=ff[1]),
            screen.height,
            fc[1]),
        Mirage(
            screen,
            FigletText(fb[2], font=ff[2]),
            screen.height + fp[2],
            fc[2]),
        Mirage(
            screen,
            FigletText(fb[3], font=ff[3]),
            screen.height + fp[3],
            fc[3]),
        Mirage(
            screen,
            FigletText(fb[4], font=ff[4]),
            screen.height + fp[4],
            fc[4]),
        Mirage(
            screen,
            FigletText(fb[5], font=ff[5]),
            screen.height + fp[5],
            fc[5]),
        Mirage(
            screen,
            FigletText(fb[6], font=ff[6]),
            screen.height + fp[6],
            fc[6]),
        Mirage(
            screen,
            FigletText(fb[7], font=ff[7]),
            screen.height + fp[7],
            fc[7]),
        Mirage(
            screen,
            FigletText(fb[8], font=ff[8]),
            screen.height + fp[8],
            fc[8]),
        Mirage(
            screen,
            FigletText(fb[9], font=ff[9]),
            screen.height + fp[9],
            fc[9]),
        Mirage(
            screen,
            FigletText(fb[10], font=ff[10]),
            screen.height + fp[10],
            fc[10]),
        Mirage(
            screen,
            FigletText(fb[11], font=ff[11]),
            screen.height + fp[11],
            fc[11]),
        Mirage(
            screen,
            FigletText(fb[12], font=ff[12]),
            screen.height + fp[12],
            fc[12]),
        Mirage(
            screen,
            FigletText(fb[13], font=ff[13]),
            screen.height + fp[13],
            fc[13]),
        Mirage(
            screen,
            FigletText(fb[14], font=ff[14]),
            screen.height + fp[14],
            fc[14]),
        Mirage(
            screen,
            FigletText(fb[15], font=ff[15]),
            screen.height + fp[15],
            fc[15]),
        Mirage(
            screen,
            FigletText(fb[16], font=ff[16]),
            screen.height + fp[16],
            fc[16]),
        Mirage(
            screen,
            FigletText(fb[17], font=ff[17]),
            screen.height + fp[17],
            fc[17]),
        Mirage(
            screen,
            FigletText(fb[18], font=ff[18]),
            screen.height + fp[18],
            fc[18]),
        Mirage(
            screen,
            FigletText(fb[19], font=ff[19]),
            screen.height + fp[19],
            fc[19]),
        Mirage(
            screen,
            FigletText(fb[20], font=ff[20]),
            screen.height + fp[20],
            fc[20]),
        Mirage(
            screen,
            FigletText(fb[21], font=ff[21]),
            screen.height + fp[21],
            fc[21]),
        Mirage(
            screen,
            FigletText(fb[22], font=ff[22]),
            screen.height + fp[22],
            fc[22]),
        Mirage(
            screen,
            FigletText(fb[23], font=ff[23]),
            screen.height + fp[23],
            fc[23]),
        Mirage(
            screen,
            FigletText(fb[24], font=ff[24]),
            screen.height + fp[24],
            fc[24]),
        Mirage(
            screen,
            FigletText(fb[25], font=ff[25]),
            screen.height + fp[25],
            fc[25]),
        Mirage(
            screen,
            FigletText(fb[26], font=ff[26]),
            screen.height + fp[26],
            fc[26]),
        Mirage(
            screen,
            FigletText(fb[27], font=ff[27]),
            screen.height + fp[27],
            fc[27]),
        Mirage(
            screen,
            FigletText(fb[28], font=ff[28]),
            screen.height + fp[28],
            fc[28]),
        Mirage(
            screen,
            FigletText(fb[29], font=ff[29]),
            screen.height + fp[29],
            fc[29]),
        Mirage(
            screen,
            FigletText(fb[30], font=ff[30]),
            screen.height + fp[30],
            fc[30]),
        Mirage(
            screen,
            FigletText(fb[31], font=ff[31]),
            screen.height + fp[31],
            fc[31]),
        Mirage(
            screen,
            FigletText(fb[32], font=ff[32]),
            screen.height + fp[32],
            fc[32]),
        Mirage(
            screen,
            FigletText(fb[33], font=ff[33]),
            screen.height + fp[33],
            fc[33]),
        Mirage(
            screen,
            FigletText(fb[34], font=ff[34]),
            screen.height + fp[34],
            fc[34]),
        Mirage(
            screen,
            FigletText(fb[35], font=ff[35]),
            screen.height + fp[35],
            fc[35]),
        Mirage(
            screen,
            FigletText(fb[36], font=ff[36]),
            screen.height + fp[36],
            fc[36]),
        Mirage(
            screen,
            FigletText(fb[37], font=ff[37]),
            screen.height + fp[37],
            fc[37]),
        Mirage(
            screen,
            FigletText(fb[38], font=ff[38]),
            screen.height + fp[38],
            fc[38]),
        Mirage(
            screen,
            FigletText(fb[39], font=ff[39]),
            screen.height + fp[39],
            fc[39]),
        Mirage(
            screen,
            FigletText(fb[40], font=ff[40]),
            screen.height + fp[40],
            fc[40]),
        Mirage(
            screen,
            FigletText(fb[41], font=ff[41]),
            screen.height + fp[41],
            fc[41]),
        Mirage(
            screen,
            FigletText(fb[42], font=ff[42]),
            screen.height + fp[42],
            fc[42]),
        Mirage(
            screen,
            FigletText(fb[43], font=ff[43]),
            screen.height + fp[43],
            fc[43]),
        Mirage(
            screen,
            FigletText(fb[44], font=ff[44]),
            screen.height + fp[44],
            fc[44]),
        Mirage(
            screen,
            FigletText(fb[45], font=ff[45]),
            screen.height + fp[45],
            fc[45]),
        Mirage(
            screen,
            FigletText(fb[46], font=ff[46]),
            screen.height + fp[46],
            fc[46]),
        Mirage(
            screen,
            FigletText(fb[47], font=ff[47]),
            screen.height + fp[47],
            fc[47]),
        Mirage(
            screen,
            FigletText(fb[48], font=ff[48]),
            screen.height + fp[48],
            fc[48]),
        Mirage(
            screen,
            FigletText(fb[49], font=ff[49]),
            screen.height + fp[49],
            fc[49]),
        Mirage(
            screen,
            FigletText(fb[50], font=ff[50]),
            screen.height + fp[50],
            fc[50]),
        Mirage(
            screen,
            FigletText(fb[51], font=ff[51]),
            screen.height + fp[51],
            fc[51]),
        Mirage(
            screen,
            FigletText(fb[52], font=ff[52]),
            screen.height + fp[52],
            fc[52]),
        Mirage(
            screen,
            FigletText(fb[53], font=ff[53]),
            screen.height + fp[53],
            fc[53]),
        Mirage(
            screen,
            FigletText(fb[54], font=ff[54]),
            screen.height + fp[54],
            fc[54]),
        Mirage(
            screen,
            FigletText(fb[55], font=ff[55]),
            screen.height + fp[55],
            fc[55]),
        Mirage(
            screen,
            FigletText(fb[56], font=ff[56]),
            screen.height + fp[56],
            fc[56]),
        Mirage(
            screen,
            FigletText(fb[57], font=ff[57]),
            screen.height + fp[57],
            fc[57]),
        Mirage(
            screen,
            FigletText(fb[58], font=ff[58]),
            screen.height + fp[58],
            fc[58]),
        Mirage(
            screen,
            FigletText(fb[59], font=ff[59]),
            screen.height + fp[59],
            fc[59]),
        Mirage(
            screen,
            FigletText(fb[60], font=ff[60]),
            screen.height + fp[60],
            fc[60]),
        Mirage(
            screen,
            FigletText(fb[61], font=ff[61]),
            screen.height + fp[61],
            fc[61]),
        Mirage(
            screen,
            FigletText(fb[62], font=ff[62]),
            screen.height + fp[62],
            fc[62]),
        Mirage(
            screen,
            FigletText(fb[63], font=ff[63]),
            screen.height + fp[63],
            fc[63]),
        Mirage(
            screen,
            FigletText(fb[64], font=ff[64]),
            screen.height + fp[64],
            fc[64]),
        Mirage(
            screen,
            FigletText(fb[65], font=ff[65]),
            screen.height + fp[65],
            fc[65]),
        Mirage(
            screen,
            FigletText(fb[66], font=ff[66]),
            screen.height + fp[66],
            fc[66]),
        Mirage(
            screen,
            FigletText(fb[67], font=ff[67]),
            screen.height + fp[67],
            fc[67]),
        Mirage(
            screen,
            FigletText(fb[68], font=ff[68]),
            screen.height + fp[68],
            fc[68]),
        Mirage(
            screen,
            FigletText(fb[69], font=ff[69]),
            screen.height + fp[69],
            fc[69]),
        Mirage(
            screen,
            FigletText(fb[70], font=ff[70]),
            screen.height + fp[70],
            fc[70]),
        Mirage(
            screen,
            FigletText(fb[71], font=ff[71]),
            screen.height + fp[71],
            fc[71]),
        Mirage(
            screen,
            FigletText(fb[72], font=ff[72]),
            screen.height + fp[72],
            fc[72]),
        Mirage(
            screen,
            FigletText(fb[73], font=ff[73]),
            screen.height + fp[73],
            fc[73]),
        Mirage(
            screen,
            FigletText(fb[74], font=ff[74]),
            screen.height + fp[74],
            fc[74]),
        Mirage(
            screen,
            FigletText(fb[75], font=ff[75]),
            screen.height + fp[75],
            fc[75]),
        Mirage(
            screen,
            FigletText(fb[76], font=ff[76]),
            screen.height + fp[76],
            fc[76]),
        Mirage(
            screen,
            FigletText(fb[77], font=ff[77]),
            screen.height + fp[77],
            fc[77]),
        Mirage(
            screen,
            FigletText(fb[78], font=ff[78]),
            screen.height + fp[78],
            fc[78]),
        Mirage(
            screen,
            FigletText(fb[79], font=ff[79]),
            screen.height + fp[79],
            fc[79]),
        Mirage(
            screen,
            FigletText(fb[80], font=ff[80]),
            screen.height + fp[80],
            fc[80]),
        Mirage(
            screen,
            FigletText(fb[81], font=ff[81]),
            screen.height + fp[81],
            fc[81]),
        Mirage(
            screen,
            FigletText(fb[82], font=ff[82]),
            screen.height + fp[82],
            fc[82]),
        Mirage(
            screen,
            FigletText(fb[83], font=ff[83]),
            screen.height + fp[83],
            fc[83]),
        Mirage(
            screen,
            FigletText(fb[84], font=ff[84]),
            screen.height + fp[84],
            fc[84]),
        Mirage(
            screen,
            FigletText(fb[85], font=ff[85]),
            screen.height + fp[85],
            fc[85]),
        Mirage(
            screen,
            FigletText(fb[86], font=ff[86]),
            screen.height + fp[86],
            fc[86]),
        Mirage(
            screen,
            FigletText(fb[87], font=ff[87]),
            screen.height + fp[87],
            fc[87]),
        Mirage(
            screen,
            FigletText(fb[88], font=ff[88]),
            screen.height + fp[88],
            fc[88]),
        Mirage(
            screen,
            FigletText(fb[89], font=ff[89]),
            screen.height + fp[89],
            fc[89]),
        Mirage(
            screen,
            FigletText(fb[90], font=ff[90]),
            screen.height + fp[90],
            fc[90]),
        Mirage(
            screen,
            FigletText(fb[91], font=ff[91]),
            screen.height + fp[91],
            fc[91]),
        Mirage(
            screen,
            FigletText(fb[92], font=ff[92]),
            screen.height + fp[92],
            fc[92]),
        Mirage(
            screen,
            FigletText(fb[93], font=ff[93]),
            screen.height + fp[93],
            fc[93]),
        Mirage(
            screen,
            FigletText(fb[94], font=ff[94]),
            screen.height + fp[94],
            fc[94]),
        Mirage(
            screen,
            FigletText(fb[95], font=ff[95]),
            screen.height + fp[95],
            fc[95]),
        Mirage(
            screen,
            FigletText(fb[96], font=ff[96]),
            screen.height + fp[96],
            fc[96]),
        Mirage(
            screen,
            FigletText(fb[97], font=ff[97]),
            screen.height + fp[97],
            fc[97]),
        Mirage(
            screen,
            FigletText(fb[98], font=ff[98]),
            screen.height + fp[98],
            fc[98]),
        Mirage(
            screen,
            FigletText(fb[99], font=ff[99]),
            screen.height + fp[99],
            fc[99]),
        Mirage(
            screen,
            FigletText(fb[100], font=ff[100]),
            screen.height + fp[100],
            fc[100])
    ]
    scenes.append(Scene(effects, (screen.height + 104) * 16))

    screen.play(scenes, stop_on_resize=True)


if __name__ == "__main__":
    while True:
        try:
            Screen.wrapper(_fizzbuzz)
            sys.exit(0)
        except ResizeScreenError:
            pass
