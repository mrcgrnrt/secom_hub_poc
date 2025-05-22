# Getting Started

In the root of the project directory, please run:

### `npm install`

This will install all the necessary dependencies.

### `npm start`

Launches the application.

## Troutbleshooting

There might be a problem installing the right dependencies with  `npm install`. 

First try to remove the file `package-lock.json`. It pins not only the versions but also the source registries. The Infineon internal registry is not available from the internet. Removing `package-lock.json` forces `npm install` to load the files from the default registries.

If this still not works (incompatible or missing packages) you can download the content of the `node_modules` folder of a running instance from the following URL: [https://marco.grunert.dev/secom_ui_node_modules.tar.gz](https://marco.grunert.dev/secom_ui_node_modules.tar.gz). Save the original `node_modules` folder and use that one from the downloaded archive.
