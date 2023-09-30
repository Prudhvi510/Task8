class TV:
    def __init__(self, brand):
        self.brand = brand
        self.channel = 1
        self.price = 0  # You can set a default price here
        self.inches = 0  # You can set a default inches value here
        self.on_off = False
        self.volume = 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:
            self.channel = channel

    def reset_tv(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        return f"{self.brand} at channel {self.channel}, volume {self.volume}"


class LedTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0
        self.backlight = False

    def display_details(self):
        return f"Brand: {self.brand}\nScreen Thickness: {self.screen_thickness} inches\nEnergy Usage: {self.energy_usage} watts\nLifespan: {self.lifespan} years\nRefresh Rate: {self.refresh_rate} Hz\nViewing Angle: {self.viewing_angle} degrees\nBacklight: {'On' if self.backlight else 'Off'}"


class PlasmaTV(TV):
    def __init__(self, brand, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate
        self.viewing_angle = 0
        self.display_details = ""

    def display_details(self):
        return f"Brand: {self.brand}\nScreen Thickness: {self.screen_thickness} inches\nEnergy Usage: {self.energy_usage} watts\nLifespan: {self.lifespan} years\nRefresh Rate: {self.refresh_rate} Hz\nViewing Angle: {self.viewing_angle} degrees\nDisplay Details: {self.display_details}"

if __name__ == "__main__":
    led_tv = LedTV("Sony", 1.2, 100, 5, 120)
    plasma_tv = PlasmaTV("Panasonic", 1.5, 150, 6, 60)

    print(led_tv.status())
    print(led_tv.display_details())

    print(plasma_tv.status())
    print(plasma_tv.display_details())