![mc-moji banner](https://i.imgur.com/gBlw9q9.png)
# mc-moji

mc-moji is a tool for creating quick skin art based on Minecraft skins. 
It is customizable based on overlays, shadows, and size.
The skin art is inspired by  [this article](https://hypixel.net/threads/guide-how-to-make-minecraft-pixel-profile-pictures-free.3747196/).

## Preview
![example](https://i.imgur.com/HmGxIF5.png)
## Installation
To install the package, clone the repository and use `pip` to install it locally:

```bash
git clone https://github.com/yourusername/mc-moji.git
cd mc-moji
pip install .
```

## Usage

Once installed, you can use the `mc-moji` command to generate skin art. Below are some examples of how to use the command.

### Recommended Usage
The command below will give the best results on average:
```bash
mc-moji [your name] -o -s -z 30
```
... or
```bash
mc-moji [your name] --overlay --shadows --size 30
```

### Basic Usage

Generate a skin art from a Minecraft username

```bash
mc-moji Steve
```
... or from a file path.
```bash
mc-moji Steve.png
```
### Adding Shadows

To add shadows to the skin:

```bash
mc-moji Steve.png --shadows
```

### Adding Overlays

To add overlays to the skin:

```bash
mc-moji Steve.png --overlay
```

### Customizing Image Size

Specify the size of the generated image (size will be 11n x 16n, to ensure correct scaling):

```bash
mc-moji Steve --size 2
```
### Multiple Skins
You can enter as many names you want.
```bash
mc-moji Stexe Alex Herobrine --size 10
```
## Contact

For any questions, reach out to [bram@gelebeer.nl](mailto:bram@gelebeer.nl).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

