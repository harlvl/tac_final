import yaml
with open("data.yaml", 'r') as stream:
    num_classes = str(yaml.safe_load(stream)['nc'])

####
#Personalizar el modelo con los valores que deseemos
####

# configurar writefile para escribir variables
from IPython.core.magic import register_line_cell_magic

@register_line_cell_magic
def writetemplate(line, cell):
    with open(line, 'w') as f:
        f.write(cell.format(**globals()))


####
#Entrenamiento de 500 epocas
####

## ejecutar en el directorio donde 
# python train.py --img 416 --batch 16 --epochs 500 --data 'dataset\data.yaml' --cfg models\custom_yolov5s.yaml --weights '' --name yolov5s_results  --cache