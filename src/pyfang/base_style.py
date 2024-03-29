from dataclasses import dataclass
from typing import ClassVar


class Selector:
    CLASS = "."
    ELEMENT = ELE = ""
    ID = "#"
    ALL = "*"


@dataclass
class BaseStyle:
    global_style_list: ClassVar[dict[str, __qualname__]] = {}
    class_name: str
    selector: str = Selector.CLASS
    align_content: str = None
    align_items: str = None
    align_self: str = None
    alignment_adjust: str = None
    alignment_baseline: str = None
    all: str = None
    alt: str = None
    animation: str = None
    animation_delay: str = None
    animation_direction: str = None
    animation_duration: str = None
    animation_fill_mode: str = None
    animation_iteration_count: str = None
    animation_name: str = None
    animation_play_state: str = None
    animation_timing_function: str = None
    azimuth: str = None

    backface_visibility: str = None
    background: str = None
    background_attachment: str = None
    background_clip: str = None
    background_color: str = None
    background_image: str = None
    background_origin: str = None
    background_position: str = None
    background_repeat: str = None
    background_size: str = None
    background_blend_mode: str = None
    baseline_shift: str = None
    bleed: str = None
    bookmark_label: str = None
    bookmark_level: str = None
    bookmark_state: str = None
    border: str = None
    border_color: str = None
    border_style: str = None
    border_width: str = None
    border_bottom: str = None
    border_bottom_color: str = None
    border_bottom_style: str = None
    border_bottom_width: str = None
    border_left: str = None
    border_left_color: str = None
    border_left_style: str = None
    border_left_width: str = None
    border_right: str = None
    border_right_color: str = None
    border_right_style: str = None
    border_right_width: str = None
    border_top: str = None
    border_top_color: str = None
    border_top_style: str = None
    border_top_width: str = None
    border_collapse: str = None
    border_image: str = None
    border_image_outset: str = None
    border_image_repeat: str = None
    border_image_slice: str = None
    border_image_source: str = None
    border_image_width: str = None
    border_radius: str = None
    border_bottom_left_radius: str = None
    border_bottom_right_radius: str = None
    border_top_left_radius: str = None
    border_top_right_radius: str = None
    border_spacing: str = None
    bottom: str = None
    box_decoration_break: str = None
    box_shadow: str = None
    box_sizing: str = None
    box_snap: str = None
    break_after: str = None
    break_before: str = None
    break_inside: str = None
    buffered_rendering: str = None

    caption_side: str = None
    clear: str = None
    clear_side: str = None
    clip: str = None
    clip_path: str = None
    clip_rule: str = None
    color: str = None
    color_adjust: str = None
    color_correction: str = None
    color_interpolation: str = None
    color_interpolation_filters: str = None
    color_profile: str = None
    color_rendering: str = None
    column_fill: str = None
    column_gap: str = None
    column_rule: str = None
    column_rule_color: str = None
    column_rule_style: str = None
    column_rule_width: str = None
    column_span: str = None
    columns: str = None
    column_count: str = None
    column_width: str = None
    contain: str = None
    content: str = None
    counter_increment: str = None
    counter_reset: str = None
    counter_set: str = None
    cue: str = None
    cue_after: str = None
    cue_before: str = None
    cursor: str = None

    direction: str = None
    display: str = None
    display_inside: str = None
    display_outside: str = None
    display_extras: str = None
    display_box: str = None
    dominant_baseline: str = None

    elevation: str = None
    empty_cells: str = None
    enable_background: str = None

    fill: str = None
    fill_opacity: str = None
    fill_rule: str = None
    filter: str = None
    float: str = None
    float_defer_column: str = None
    float_defer_page: str = None
    float_offset: str = None
    float_wrap: str = None
    flow_into: str = None
    flow_from: str = None
    flex: str = None
    flex_basis: str = None
    flex_grow: str = None
    flex_shrink: str = None
    flex_flow: str = None
    flex_direction: str = None
    flex_wrap: str = None
    flood_color: str = None
    flood_opacity: str = None
    font: str = None
    font_family: str = None
    font_size: str = None
    font_stretch: str = None
    font_style: str = None
    font_weight: str = None
    font_feature_settings: str = None
    font_kerning: str = None
    font_language_override: str = None
    font_size_adjust: str = None
    font_synthesis: str = None
    font_variant: str = None
    font_variant_alternates: str = None
    font_variant_caps: str = None
    font_variant_east_asian: str = None
    font_variant_ligatures: str = None
    font_variant_numeric: str = None
    font_variant_position: str = None
    footnote_policy: str = None

    glyph_orientation_horizontal: str = None
    glyph_orientation_vertical: str = None
    grid: str = None
    grid_auto_flow: str = None
    grid_auto_columns: str = None
    grid_auto_rows: str = None
    grid_template: str = None
    grid_template_areas: str = None
    grid_template_columns: str = None
    grid_template_rows: str = None
    grid_area: str = None
    grid_column: str = None
    grid_column_start: str = None
    grid_column_end: str = None
    grid_row: str = None
    grid_row_start: str = None
    grid_row_end: str = None
    grid_gap: str = None

    hanging_punctuation: str = None
    height: str = None
    hyphenate_character: str = None
    hyphenate_limit_chars: str = None
    hyphenate_limit_last: str = None
    hyphenate_limit_lines: str = None
    hyphenate_limit_zone: str = None
    hyphens: str = None

    icon: str = None
    image_orientation: str = None
    image_resolution: str = None
    image_rendering: str = None
    ime: str = None
    ime_align: str = None
    ime_mode: str = None
    ime_offset: str = None
    ime_width: str = None
    initial_letters: str = None
    inline_box_align: str = None
    isolation: str = None

    justify_content: str = None
    justify_items: str = None
    justify_self: str = None

    kerning: str = None

    left: str = None
    letter_spacing: str = None
    lighting_color: str = None
    line_box_contain: str = None
    line_break: str = None
    line_grid: str = None
    line_height: str = None
    line_slack: str = None
    line_snap: str = None
    list_style: str = None
    list_style_image: str = None
    list_style_position: str = None
    list_style_type: str = None

    margin: str = None
    margin_bottom: str = None
    margin_left: str = None
    margin_right: str = None
    margin_top: str = None
    marker: str = None
    marker_end: str = None
    marker_mid: str = None
    marker_pattern: str = None
    marker_segment: str = None
    marker_start: str = None
    marker_knockout_left: str = None
    marker_knockout_right: str = None
    marker_side: str = None
    marks: str = None
    marquee_direction: str = None
    marquee_play_count: str = None
    marquee_speed: str = None
    marquee_style: str = None
    mask: str = None
    mask_image: str = None
    mask_repeat: str = None
    mask_position: str = None
    mask_clip: str = None
    mask_origin: str = None
    mask_size: str = None
    mask_box: str = None
    mask_box_outset: str = None
    mask_box_repeat: str = None
    mask_box_slice: str = None
    mask_box_source: str = None
    mask_box_width: str = None
    mask_type: str = None
    max_height: str = None
    max_lines: str = None
    max_width: str = None
    min_height: str = None
    min_width: str = None
    mix_blend_mode: str = None

    nav_down: str = None
    nav_index: str = None
    nav_left: str = None
    nav_right: str = None
    nav_up: str = None

    object_fit: str = None
    object_position: str = None
    offset_after: str = None
    offset_before: str = None
    offset_end: str = None
    offset_start: str = None
    opacity: str = None
    order: str = None
    orphans: str = None
    outline: str = None
    outline_color: str = None
    outline_style: str = None
    outline_width: str = None
    outline_offset: str = None
    overflow: str = None
    overflow_x: str = None
    overflow_y: str = None
    overflow_style: str = None
    overflow_wrap: str = None

    padding: str = None
    padding_bottom: str = None
    padding_left: str = None
    padding_right: str = None
    padding_top: str = None
    page: str = None
    page_break_after: str = None
    page_break_before: str = None
    page_break_inside: str = None
    paint_order: str = None
    pause: str = None
    pause_after: str = None
    pause_before: str = None
    perspective: str = None
    perspective_origin: str = None
    pitch: str = None
    pitch_range: str = None
    play_during: str = None
    pointer_events: str = None
    position: str = None

    quotes: str = None

    region_fragment: str = None
    resize: str = None
    rest: str = None
    rest_after: str = None
    rest_before: str = None
    richness: str = None
    right: str = None
    ruby_align: str = None
    ruby_merge: str = None
    ruby_position: str = None

    scroll_behavior: str = None
    scroll_snap_coordinate: str = None
    scroll_snap_destination: str = None
    scroll_snap_points_x: str = None
    scroll_snap_points_y: str = None
    scroll_snap_type: str = None
    shape_image_threshold: str = None
    shape_inside: str = None
    shape_margin: str = None
    shape_outside: str = None
    shape_padding: str = None
    shape_rendering: str = None
    size: str = None
    speak: str = None
    speak_as: str = None
    speak_header: str = None
    speak_numeral: str = None
    speak_punctuation: str = None
    speech_rate: str = None
    src: str = None
    stop_color: str = None
    stop_opacity: str = None
    stress: str = None
    string_set: str = None
    stroke: str = None
    stroke_dasharray: str = None
    stroke_dashoffset: str = None
    stroke_linecap: str = None
    stroke_linejoin: str = None
    stroke_miterlimit: str = None
    stroke_opacity: str = None
    stroke_width: str = None

    tab_size: str = None
    table_layout: str = None
    text_align: str = None
    text_align_all: str = None
    text_align_last: str = None
    text_anchor: str = None
    text_combine_upright: str = None
    text_decoration: str = None
    text_decoration_color: str = None
    text_decoration_line: str = None
    text_decoration_style: str = None
    text_decoration_skip: str = None
    text_emphasis: str = None
    text_emphasis_color: str = None
    text_emphasis_style: str = None
    text_emphasis_position: str = None
    text_emphasis_skip: str = None
    text_height: str = None
    text_indent: str = None
    text_justify: str = None
    text_orientation: str = None
    text_overflow: str = None
    text_rendering: str = None
    text_shadow: str = None
    text_size_adjust: str = None
    text_space_collapse: str = None
    text_spacing: str = None
    text_transform: str = None
    text_underline_position: str = None
    text_wrap: str = None
    top: str = None
    touch_action: str = None
    transform: str = None
    transform_box: str = None
    transform_origin: str = None
    transform_style: str = None
    transition: str = None
    transition_delay: str = None
    transition_duration: str = None
    transition_property: str = None
    transition_timing_function: str = None

    unicode_bidi: str = None

    vector_effect: str = None
    vertical_align: str = None
    visibility: str = None
    voice_balance: str = None
    voice_duration: str = None
    voice_family: str = None
    voice_pitch: str = None
    voice_range: str = None
    voice_rate: str = None
    voice_stress: str = None
    voice_volumn: str = None
    volume: str = None

    white_space: str = None
    widows: str = None
    width: str = None
    will_change: str = None
    word_break: str = None
    word_spacing: str = None
    word_wrap: str = None
    wrap_flow: str = None
    wrap_through: str = None
    writing_mode: str = None

    z_index: str = None

    def __post_init__(self) -> None:
        if self.class_name in self.global_style_list:
            raise ValueError(f"{self.class_name} already exists")
        else:
            self.global_style_list[self.class_name] = self

    def __str__(self) -> str:
        return ";".join(
            [f"{key}:{val}" for key, val in vars(self).items() if val is not None]
        )

    def create_class(self) -> str:
        prop_map = vars(self)
        selector = prop_map.pop("selector")
        class_name = prop_map.pop("class_name")

        props = "".join(
            (
                f'  {key.replace("_", "-")}:{val};\n'
                for key, val in prop_map.items()
                if val is not None
            )
        )

        vars(self)["selector"] = selector
        vars(self)["class_name"] = class_name

        return f"{self.selector}{class_name} {{\n{props}\n}}"

    @classmethod
    def to_css(cls, file_name: str) -> None:
        file_str = ""
        for _, style in cls.global_style_list.items():
            file_str = "\n".join((file_str, style.create_class()))

        with open(file_name + ".css", "w") as f:
            f.write(file_str)


class FontFace(BaseStyle):
    def __init__(self, font_family: str, src: str) -> None:
        super().__init__(
            "font-face", selector="@", font_family=f'"{font_family}"', src=src
        )
