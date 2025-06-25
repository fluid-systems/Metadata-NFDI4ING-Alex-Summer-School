from reportlab.lib.units import cm


class SupportedTemplate:
    def __init__(self,
                 LABEL_SIZE,
                 RECOMMENDED_MAX_LABEL_PRINT_SIZE,
                 ROW_MAX_LABEL_COUNT,
                 COLUMN_MAX_LABEL_COUNT,
                 MEASURED_START_POSITION,
                 MEASURED_x_DISTANCE_PER_STEP,
                 MEASURED_y_DISTANCE_PER_STEP):

        self.LABEL_SIZE = LABEL_SIZE
        self.RECOMMENDED_MAX_LABEL_PRINT_SIZE = RECOMMENDED_MAX_LABEL_PRINT_SIZE
        self.ROW_MAX_LABEL_COUNT = ROW_MAX_LABEL_COUNT
        self.COLUMN_MAX_LABEL_COUNT = COLUMN_MAX_LABEL_COUNT
        self.MEASURED_START_POSITION = MEASURED_START_POSITION
        self.MEASURED_x_DISTANCE_PER_STEP = MEASURED_x_DISTANCE_PER_STEP
        self.MEASURED_y_DISTANCE_PER_STEP = MEASURED_y_DISTANCE_PER_STEP

SUPPORTED_TEMPLATES = {
    ## AVERY Zweckform B7651 (Sensor p_ID Labels)
    'B7651': SupportedTemplate(LABEL_SIZE=  (3.8 * cm, 2.1 * cm),
                               RECOMMENDED_MAX_LABEL_PRINT_SIZE=  (3.35 * cm, 1.65 * cm),
                               ROW_MAX_LABEL_COUNT=  13,
                               COLUMN_MAX_LABEL_COUNT=  5,
                               MEASURED_START_POSITION=  (0.65 * cm, (29.7 - 3) * cm),
                               MEASURED_x_DISTANCE_PER_STEP=  4.06 * cm,
                               MEASURED_y_DISTANCE_PER_STEP=  -2.12 * cm,
    ),
    ## AVERY Zweckform L6011
    'L6011': SupportedTemplate(LABEL_SIZE=  (6.35 * cm, 2.96 * cm),
                               RECOMMENDED_MAX_LABEL_PRINT_SIZE=  (5.9 * cm, 2.5 * cm),
                               ROW_MAX_LABEL_COUNT=  9,
                               COLUMN_MAX_LABEL_COUNT=  3,
                               MEASURED_START_POSITION=  (0.91 * cm, (29.7 - 4.27) * cm),
                               MEASURED_x_DISTANCE_PER_STEP=  6.6 * cm,
                               MEASURED_y_DISTANCE_PER_STEP=  -2.96 * cm,
                               ),
    ## AVERY Zweckform L6009
    'L6009': SupportedTemplate(LABEL_SIZE=  (4.57 * cm, 2.12 * cm),
                               RECOMMENDED_MAX_LABEL_PRINT_SIZE=  (4.08 * cm, 1.62 * cm),
                               ROW_MAX_LABEL_COUNT=  12,
                               COLUMN_MAX_LABEL_COUNT=  4,
                               MEASURED_START_POSITION=  (1.19 * cm, (29.7 - 4.022) * cm),
                               MEASURED_x_DISTANCE_PER_STEP=  4.83 * cm,
                               MEASURED_y_DISTANCE_PER_STEP=  -2.117 * cm,
                               ),
}
