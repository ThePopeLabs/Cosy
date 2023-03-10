import tensorflow as tf
import pytest
import numpy as np
from cosy.models import CosyNet, CosyNetMultiInput
from cosy.losses import squared_frobenius_norm


@pytest.fixture
def test_mlp():
    input_ = tf.keras.Input(shape=(10,))
    x = tf.keras.layers.Dense(10)(input_)
    x = tf.keras.layers.Dense(10)(x)
    x = tf.keras.layers.Dense(10)(x)
    x = tf.keras.layers.Dense(10)(x)
    out = tf.keras.layers.Dense(1)(x)
    return tf.keras.Model(inputs=input_, outputs=out)


@pytest.fixture
def cosy_net_params(test_mlp):
    return {
        "model_config": [test_mlp.get_config()] * 3,
        "max_layer_cutoff": -1,
        "min_layer_cutoff": 0,
        "loss_fn": squared_frobenius_norm,
        "scalar": [0.2, 0.2, 0.2],
    }


@pytest.fixture(autouse=True)
def cosy_net_obj(cosy_net_params):
    return CosyNet(**cosy_net_params)


@pytest.fixture(autouse=True)
def cosy_net_multi_input_obj(cosy_net_params):
    return CosyNetMultiInput(**cosy_net_params)


@pytest.fixture
def network_params_ones():
    return [
        [tf.ones((2, 2)), tf.ones((2, 2)), tf.ones((2, 2))],
        [tf.ones((2, 2)), tf.ones((2, 2)), tf.ones((2, 2))],
        [tf.ones((2, 2)), tf.ones((2, 2)), tf.ones((2, 2))],
    ]


@pytest.fixture
def network_params_zeros():
    return [
        [tf.zeros((2, 2)), tf.zeros((2, 2)), tf.zeros((2, 2))],
        [tf.zeros((2, 2)), tf.zeros((2, 2)), tf.zeros((2, 2))],
        [tf.zeros((2, 2)), tf.zeros((2, 2)), tf.zeros((2, 2))],
    ]


@pytest.fixture
def network_params_alternate():
    return [
        [tf.zeros((2, 2)), tf.ones((2, 2)), tf.zeros((2, 2))],
        [tf.ones((2, 2)), tf.ones((2, 2)), tf.ones((2, 2))],
        [tf.ones((2, 2)), tf.zeros((2, 2)), tf.ones((2, 2))],
    ]


@pytest.fixture
def network_params_random_deterministic():
    tf.random.set_seed(42)

    return [
        [
            tf.random.uniform((2, 2)),
            tf.random.uniform((2, 2)),
            tf.random.uniform((2, 2)),
        ],
        [
            tf.random.uniform((2, 2)),
            tf.random.uniform((2, 2)),
            tf.random.uniform((2, 2)),
        ],
        [
            tf.random.uniform((2, 2)),
            tf.random.uniform((2, 2)),
            tf.random.uniform((2, 2)),
        ],
    ]


@pytest.fixture
def weights_2d():
    return np.array([[[1, 2], [1, 2]], [[3, 4], [3, 4]]])


@pytest.fixture
def weights_2d_identical():
    return np.array([[[1, 2], [1, 2]], [[1, 2], [1, 2]]])


@pytest.fixture
def weights_3d():
    return np.array([[[1, 2], [1, 2]], [[3, 4], [3, 4]], [[5, 6], [5, 6]]])


@pytest.fixture
def weights_4d():
    return np.array(
        [[[1, 2], [1, 2]], [[3, 4], [3, 4]], [[5, 6], [5, 6]], [[7, 8], [7, 8]]]
    )
