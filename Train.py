def train(generator, discriminator, g_optimizer, d_optimizer, dataloader, criterion, generator_loss, epochs=1):
    for epoch in range(epochs):
        for real_images, target_positions in dataloader:  # 假设dataloader同时提供图像和目标位置
            # 训练判别器
            d_optimizer.zero_grad()
            real_loss = criterion(discriminator(real_images), torch.ones(real_images.size(0), 1, device=real_images.device))
            fake_images = generator(real_images)
            fake_loss = criterion(discriminator(fake_images.detach()), torch.zeros(real_images.size(0), 1, device=real_images.device))
            d_loss = (real_loss + fake_loss) / 2
            d_loss.backward()
            d_optimizer.step()

            # 更新生成器
            g_optimizer.zero_grad()
            # 注意：这里应该调用你自定义的 generator_loss 函数，它可能会结合对抗性损失和其他条件损失
            g_loss = generator_loss(fake_images, real_images, discriminator, target_positions)
            g_loss.backward()
            g_optimizer.step()

        print(f"Epoch {epoch+1}, D Loss: {d_loss.item()}, G Loss: {g_loss.item()}")
