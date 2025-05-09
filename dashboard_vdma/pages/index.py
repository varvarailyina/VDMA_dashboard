import reflex as rx
from dashboard_vdma import styles

def index() -> rx.Component:
    return rx.vstack(

        # top-left heading
        rx.box(
            rx.vstack(
                rx.heading("VDMA Dashboard", size="8"),
                rx.text("Welcome to the dashboard.", size="4"),
                spacing="1",
                align_items="start",
            ),
            padding="1.5em",
            width="100%",
        ),

        # main content
        rx.spacer(),

        # bottom-center links
        rx.box(
            rx.hstack(
                rx.link(
                    "About",
                    href="/about",
                    font_size="1em",
                    text_decoration="underline",
                    color=styles.accent_text_color,
                    _hover={"color": styles.hover_accent_color},
                ),
                rx.text("|", color="gray"),
                rx.link(
                    "VDMA",
                    href="https://www.vdma.org",
                    is_external=True,
                    font_size="1em",
                    text_decoration="underline",
                    color=styles.accent_text_color,
                    _hover={"color": styles.hover_accent_color},
                ),
                spacing="2",
                justify="center",
            ),
            width="100%",
            display="flex",
            justify_content="center",
            padding_bottom="1.5em",
        ),

        height="100vh",
        justify="between"
    )