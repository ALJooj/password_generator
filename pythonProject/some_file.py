import fire

# make class subcommands


class Navigator:
    def retrun_coords(self, x, y):
        print(f'coords are: {x}, {y} and {x * y}')

    def get_world_sides(self):
        sides = ['West', "East", "North", "South"]
        print(f'all the sides are: {",".join(sides)}')

# new subcommands from func
def rocker(send_to='Space'):
    print(f"send rocket to {send_to}")


class CLI():
    def __init__(self):
        self.navigator = Navigator()
        self.rocket = rocker


if __name__ == "__main__":
    fire.Fire(CLI)