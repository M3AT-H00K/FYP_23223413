import torch.nn as nn


def build_model(config):

    layers = []

    for layer in config["layers"]:

        if layer["type"] == "Conv2D":

            layers.append(
                nn.Conv2d(
                    in_channels=1,
                    out_channels=6,
                    kernel_size=5
                )
            )

        elif layer["type"] == "MaxPool2D":

            layers.append(
                nn.MaxPool2d(2)
            )

        elif layer["type"] == "Flatten":

            layers.append(
                nn.Flatten()
            )

        elif layer["type"] == "Linear":

            layers.append(
                nn.Linear(
                    576,
                    10
                )
            )

    return nn.Sequential(*layers)