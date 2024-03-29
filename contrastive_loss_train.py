
def train_contrastive(model, dataloader, loss_fn, optimizer, device):
    model.train()
    total_loss = 0.0

    for batch in tqdm(dataloader, desc="Training"):
        # Unpack data from the dataloader
        anchor, positive, negative = batch
        anchor, positive, negative = anchor.to(device), positive.to(device), negative.to(device)

        # Zero the gradients
        optimizer.zero_grad()

        # Forward pass
        outputs_anchor = model(anchor, anchor)
        outputs_positive = model(positive, positive)
        outputs_negative = model(negative, negative)

        # Compute contrastive loss
        loss = loss_fn(outputs_anchor, outputs_positive, outputs_negative)

        # Backward pass and optimization
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    return total_loss / len(default_generatorloader)

# Example usage
num_epochs = 10

for epoch in range(num_epochs):
    train_loss = train_contrastive(joint_model, dataloader, contrastive_loss, optimizer, device)
    print(f"Epoch {epoch + 1}/{num_epochs}, Training Loss: {train_loss}")
