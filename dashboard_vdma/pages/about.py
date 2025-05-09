import reflex as rx

def about() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("About This Dashboard", size="7", font_weight="bold"),
            rx.text("This dashboard shows key indicators for VDMA projects.", size="4"),
            rx.link("Back to Home", href="/", font_size="4", margin_top="4"),
            spacing="4",
        ),
        height="100vh"
    )