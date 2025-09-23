import torch
import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend for headless environments
import matplotlib.pyplot as plt


def drow(x, y, model, epoch=None):
    """
    Plots the data points, the model's prediction, and the true function.
    Optionally annotates with the current epoch.
    """
    plt.figure(figsize=(10, 6))
    # Bottom subplot: Model prediction and data
    plt.subplot(212)
    plt.plot(x.numpy(), (model.weight.item() * x).detach().numpy(), label='Model Prediction')
    plt.plot(x.numpy(), y.detach().numpy(), 'ro', label='Data')
    plt.xlabel("x")
    plt.ylim(-20, 20)
    plt.legend()

    # Top subplot: True function
    plt.subplot(211)
    title = "Data Space (top) Estimated Line (bottom)"
    if epoch is not None:
        title += f" Iteration {epoch}"
    plt.title(title)
    plt.plot(x.numpy(), (-3.0 * x).detach().numpy(), 'g--', label='True Function')
    plt.xlabel("x")
    plt.legend()
    plt.tight_layout()

    # Save plot to file (since we're in a headless environment)
    plot_filename = f'./Neural_Networks_and_PyTorch/m02/linear_regression_plot{epoch}.png'
    plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
    print(f"Plot saved to '{plot_filename}'")



# Simple linear regression model: y = w * x
class LinearRegressionModel:
    def __init__(self, initial_weight: float):
        self.weight = torch.tensor([initial_weight], requires_grad=True)

    def forward(self, x):
        return self.weight * x

    def parameters(self):
        return [self.weight]

# Generate simple linear data: y = -3x + noise
def generate_data(slope=-3.0, noise_std=0.1, num_points=60):
    x = torch.linspace(-3, 3, num_points).view(-1, 1)
    y = slope * x + noise_std * torch.randn(x.size())
    return x, y

def train(model, x, y, learning_rate=0.1, num_epochs=4):
    losses = []
    weights = []
    for epoch in range(num_epochs):
        pred = model.forward(x)
        loss = torch.mean((pred - y) ** 2)
        loss.backward()
        with torch.no_grad():
            for param in model.parameters():
                param -= learning_rate * param.grad
        for param in model.parameters():
            param.grad.zero_()
        losses.append(loss.item())
        weights.append(model.weight.item())
        print(f"Epoch {epoch+1}/{num_epochs}, Loss: {loss.item():.6f}, Weight: {model.weight.item():.4f}")
        drow(x, y, model, epoch=epoch+1)
    return losses, weights

def main():
    print("Simple Linear Regression Training Example")
    initial_weight = -10.0
    model = LinearRegressionModel(initial_weight)
    x, y = generate_data()
    print(f"Initial weight: {initial_weight}")
    losses, weights = train(model, x, y, learning_rate=0.1, num_epochs=4)
    print(f"Trained weight: {model.weight.item():.4f}")

    # Create subplots for both visualizations
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Plot 1: Data and model prediction
    ax1.scatter(x.numpy(), y.numpy(), color='red', label='Data')
    ax1.plot(x.numpy(), (model.weight.item() * x).numpy(), color='blue', label='Model Prediction')
    ax1.plot(x.numpy(), (-3.0 * x).numpy(), 'g--', label='True Function')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.legend()
    ax1.set_title('Linear Regression Fit')
    
    # Plot 2: Loss vs Weight
    ax2.plot(weights, losses, 'bo-', linewidth=2, markersize=8)
    ax2.set_xlabel('Weight')
    ax2.set_ylabel('Loss')
    ax2.set_title('Loss vs Weight During Training')
    ax2.grid(True, alpha=0.3)
    
    # Add annotations for start and end points
    ax2.annotate(f'Start\n({weights[0]:.2f}, {losses[0]:.2f})', 
                xy=(weights[0], losses[0]), xytext=(10, 10), 
                textcoords='offset points', fontsize=10,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='yellow', alpha=0.7))
    ax2.annotate(f'End\n({weights[-1]:.2f}, {losses[-1]:.2f})', 
                xy=(weights[-1], losses[-1]), xytext=(10, -20), 
                textcoords='offset points', fontsize=10,
                bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.7))
    
    plt.tight_layout()
    
    # Save plot to file (since we're in a headless environment)
    plot_filename = './Neural_Networks_and_PyTorch/m02/linear_regression_plot.png'
    plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
    print(f"Plot saved to '{plot_filename}'")
    print("Note: In headless environments, plots are saved to files instead of displayed.")

if __name__ == "__main__":
    main()

