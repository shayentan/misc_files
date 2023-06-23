import numpy as np


for i in range(300):
    sampled = np.zeros((1, maxlen, len(chars)))
    # Turn each char to char index.
    for t, char in enumerate(generated_text):
        sampled[0, t, char_indices[char]] = 1.
    # Predict next char probabilities
    preds = model.predict(sampled, verbose=0)[0]
    # Add some randomness by sampling given probabilities.
    next_index = sample(preds, temperature)
    # Turn char index to char.
    next_char = chars[next_index]
    # Append char to generated text string
    generated_text += next_char
    # Pop the first char in generated text string.
    generated_text = generated_text[1:]
    # Print the new generated char.
    sys.stdout.write(next_char)
    sys.stdout.flush()
print(generated_text)