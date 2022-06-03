import PySimpleGUI as sg

sg.theme('DarkAmber')   # Add a touch of color
sg.set_options(icon                    = None,# {{{
    button_color                    = None,
    element_size                    = (None, None),
    button_element_size             = (None, None),
    margins                         = (None, None),
    element_padding                 = (None, None),
    auto_size_text                  = None,
    auto_size_buttons               = None,
    font                            = 'Courier 22',
    border_width                    = None,
    slider_border_width             = None,
    slider_relief                   = None,
    slider_orientation              = None,
    autoclose_time                  = None,
    message_box_line_width          = None,
    progress_meter_border_depth     = None,
    progress_meter_style            = None,
    progress_meter_relief           = None,
    progress_meter_color            = None,
    progress_meter_size             = None,
    text_justification              = None,
    background_color                = None,
    element_background_color        = None,
    text_element_background_color   = None,
    input_elements_background_color = None,
    input_text_color                = None,
    scrollbar_color                 = None,
    text_color                      = None,
    element_text_color              = None,
    debug_win_size                  = (None, None),
    window_location                 = (None, None),
    error_button_color              = (None, None),
    tooltip_time                    = None,
    tooltip_font                    = None,
    use_ttk_buttons                 = None,
    ttk_theme                       = None,
    suppress_error_popups           = None,
    suppress_raise_key_errors       = None,
    suppress_key_guessing           = None,
    warn_button_key_duplicates      = False,
    enable_treeview_869_patch       = None,
    enable_mac_notitlebar_patch     = None,
    use_custom_titlebar             = None,
    titlebar_background_color       = None,
    titlebar_text_color             = None,
    titlebar_font                   = None,
    titlebar_icon                   = None,
    user_settings_path              = None,
    pysimplegui_settings_path       = None,
    pysimplegui_settings_filename   = None,
    keep_on_top                     = None,
    dpi_awareness                   = None,
    scaling                         = None,
    disable_modal_windows           = None,
    force_modal_windows             = None,
    tooltip_offset                  = (None, None),
    sbar_trough_color               = None,
    sbar_background_color           = None,
    sbar_arrow_color                = None,
    sbar_width                      = None,
    sbar_arrow_width                = None,
    sbar_frame_color                = None,
    sbar_relief                     = None
    )# }}}


# All the stuff inside your window.
layout = [  [sg.Text('Some text on Row 1')],
            [sg.Text('Enter something on Row 2'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')],
            ]

# Create the Window
window = sg.Window('Window Title', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    print('You entered ', values[0])

window.close()
