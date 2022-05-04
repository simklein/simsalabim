import numpy as np


class Signal:
    """Class for audio signals.
    Objects of this class contain data which is directly convertable between
    time and frequency domain (equally spaced samples and frequency bins).
    """
    def __init__(
            self,
            data,
            sampling_rate,
            comment=None,
            dtype=np.double):
        """Create Signal with data, and sampling rate.
        Parameters
        ----------
        data : ndarray, double
            Raw data of the signal in the time or frequency domain. The memory
            layout of data is 'C'. E.g. data of ``shape = (3, 2, 1024)`` has
            3 x 2 channels with 1024 samples.
        sampling_rate : double
            Sampling rate in Hz
        n_samples : int, optional
            Number of samples of the time signal. Required if domain is
            ``'freq'``. The default is ``None``, which assumes an even number
            of samples if the data is provided in the frequency domain.
        comment : str
            A comment related to `data`. The default is ``None``.
        dtype : string, optional
            Raw data type of the audio object. The default is `float64`
        References
        ----------
        .. [#] J. Ahrens, C. Andersson, P. Höstmad, and W. Kropp, “Tutorial on
               Scaling of the Discrete Fourier Transform and the Implied
               Physical Units of the Spectra of Time-Discrete Signals,” Vienna,
               Austria, May 2020, p. e-Brief 600.
        """
        # initializing global parameters
        self.comment = comment
        self._dtype = dtype

        # initialize signal specific parameters
        self._sampling_rate = sampling_rate

        self._data = np.asarray(data, dtype=dtype)
        self._n_samples = self._data.shape[-1]

    @property
    def data(self):
        """Get data."""
        return self._data

    @property
    def comment(self):
        """Get comment."""
        return self._comment

    @comment.setter
    def comment(self, value):
        """Set comment."""
        self._comment = 'none' if value is None else str(value)

    @property
    def dtype(self):
        """The data type of the audio object. This can be any data type and
        precision supported by numpy."""
        return self._dtype

    @property
    def n_samples(self):
        """The number of samples."""
        return self._n_samples

    @property
    def sampling_rate(self):
        """The sampling rate of the signal."""
        return self._sampling_rate

    @property
    def duration(self):
        """The duration of the signal in seconds."""
        duration = 1 / self._sampling_rate * self._n_samples
        return duration

    @sampling_rate.setter
    def sampling_rate(self, value):
        self._sampling_rate = value

    def __repr__(self):
        """String representation of Signal class."""
        repr_string = (
            f"Signal: {self.comment}\n"
            f"Audio signal with {self.n_samples} samples @ "
            f"{self._sampling_rate} Hz sampling rate\n")

        return repr_string

    def __len__(self):
        """Length of the object which is the number of samples stored.
        """
        return self.n_samples

