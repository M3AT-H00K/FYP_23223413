import torch.nn as nn


def build_model(config):

    layers = []

    for layer in config["layers"]:

        if layer["type"] == "Conv2D":

            layers.append(
                nn.Conv2d(
                    in_channels=layer["in_channels"],
                    out_channels=layer["out_channels"],
                    kernel_size=layer["kernel_size"]
                )
            )

        elif layer["type"] == "MaxPool2D":

            nn.MaxPool2d(
                layer["kernel_size"]
            )

        elif layer["type"] == "Flatten":

            layers.append(
                nn.Flatten()
            )

        elif layer["type"] == "Linear":

            layers.append(
                nn.Linear(
                    layer["in_features"],
                    layer["out_features"]
                )
            )

    return nn.Sequential(*layers)