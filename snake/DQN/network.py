import torch
import torch.nn as nn


class Network(nn.Module):
    """Neural network

    Attribute:
        in_dim (int): liczba cech wejściowych
        out_dim (int): liczba cech wyjściowych
        out_features (int): liczba cech w warstwach ukrytych
    """

    def __init__(self, in_dim: int, out_dim: int, out_features: int = 128):
        """Initialization."""
        super(Network, self).__init__()

        self.layers = nn.Sequential(
            nn.Linear(in_dim, out_features),
            nn.ReLU(),
            nn.Linear(out_features, out_features),
            nn.ReLU(),
            nn.Linear(out_features, out_dim)
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Forward method implementation."""
        return self.layers(x)